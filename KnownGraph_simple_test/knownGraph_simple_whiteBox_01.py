import unittest
from knownGraph_simple_01 import KnowledgeGraph


class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.kg = KnowledgeGraph()
        print("\n=== 初始化新知识图谱 ===")

    def test_insert_success(self):
        # 测试正常插入
        test_case = ("Apple", "is_a", "Fruit")
        print(f"\n测试插入成功案例: {test_case}")

        # 执行插入操作
        self.kg.add_triplet(*test_case)

        # 验证插入结果
        self.assertIn(test_case[0], self.kg.graph)
        self.assertIn(test_case[1], self.kg.graph[test_case[0]])
        self.assertIn(test_case[2], self.kg.graph[test_case[0]][test_case[1]])
        print("插入验证成功 → 元素存在于图谱中")

    def test_insert_failure(self):
        # 测试失败插入（类型错误）
        test_case = (123, 456, 789)
        print(f"\n测试插入失败案例（错误类型）: {test_case}")

        # 验证异常抛出
        with self.assertRaises(ValueError) as context:
            self.kg.add_triplet(*test_case)

        # 验证错误信息
        self.assertIn("All arguments must be strings", str(context.exception))
        print(f"插入失败验证成功 → 捕获异常: {context.exception}")

    def test_duplicate_insertion(self):
        # 测试重复插入
        test_case = ("Earth", "has_moon", "Moon")
        print(f"\n测试重复插入: {test_case}")

        # 第一次插入
        self.kg.add_triplet(*test_case)
        first_insert = len(self.kg.graph["Earth"]["has_moon"])

        # 第二次插入
        self.kg.add_triplet(*test_case)
        second_insert = len(self.kg.graph["Earth"]["has_moon"])

        # 验证集合大小不变
        self.assertEqual(first_insert, second_insert)
        print(f"去重验证成功 → 集合大小保持 {first_insert}")

    def test_graph_dump(self):
        # 测试图谱内容输出
        test_data = [
            ("Einstein", "developed", "Relativity"),
            ("Newton", "discovered", "Gravity"),
            ("Einstein", "won", "Nobel Prize")
        ]

        # 批量插入数据
        print("\n插入测试数据:")
        for triplet in test_data:
            self.kg.add_triplet(*triplet)
            print(f"已插入: {triplet}")

        # 验证图谱完整性
        print("\n当前知识图谱完整内容:")
        for subject in self.kg.graph:
            for relation in self.kg.graph[subject]:
                for obj in self.kg.graph[subject][relation]:
                    print(f"({subject}, {relation}, {obj})")
                    self.assertIn((subject, relation, obj), test_data)

        # 验证总数
        total = sum(len(objs) for subj in self.kg.graph.values() for objs in subj.values())
        self.assertEqual(total, len(test_data))
        print(f"\n总数验证成功 → 共 {total} 个三元组")


if __name__ == '__main__':
    unittest.main(verbosity=2)