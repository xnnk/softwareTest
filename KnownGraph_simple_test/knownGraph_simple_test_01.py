import unittest
from knownGraph_simple_01 import KnowledgeGraph

class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.kg = KnowledgeGraph()

    # 语句覆盖测试用例
    def test_add_triplet_statement_coverage(self):
        # 正常添加三元组
        self.kg.add_triplet("A", "related_to", "B")
        # 检查是否成功添加
        self.assertIn("A", self.kg.graph)
        self.assertIn("related_to", self.kg.graph["A"])
        self.assertIn("B", self.kg.graph["A"]["related_to"])

        # 添加重复的三元组（应该不报错，但集合中不会有重复项）
        self.kg.add_triplet("A", "related_to", "B")
        self.assertEqual(len(self.kg.graph["A"]["related_to"]), 1)

    # 条件覆盖测试用例
    def test_add_triplet_condition_coverage(self):
        # 类型检查失败（非字符串类型）
        with self.assertRaises(ValueError):
            self.kg.add_triplet(123, "related_to", "B")
        with self.assertRaises(ValueError):
            self.kg.add_triplet("A", 123, "B")
        with self.assertRaises(ValueError):
            self.kg.add_triplet("A", "related_to", 123)

        # 主体不存在于图中
        self.kg.add_triplet("C", "related_to", "D")
        self.assertIn("C", self.kg.graph)
        self.assertIn("related_to", self.kg.graph["C"])
        self.assertIn("D", self.kg.graph["C"]["related_to"])

        # 关系不存在于主体的关系中
        self.kg.add_triplet("E", "similar_to", "F")
        self.assertIn("E", self.kg.graph)
        self.assertIn("similar_to", self.kg.graph["E"])
        self.assertIn("F", self.kg.graph["E"]["similar_to"])


if __name__ == '__main__':
    unittest.main()