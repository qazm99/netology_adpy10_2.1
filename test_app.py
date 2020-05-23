import unittest
import app
from unittest.mock import patch


class TestApp(unittest.TestCase):
    def setUp(self):
        self.directories, self.documents = app.update_date()
        # with patch('app.update_date', return_value=(self.directories, self.documents)):
        app.documents = self.documents
        app.directories = self.directories

    def test_update_date(self):
        result_update_date = app.update_date()
        self.assertIsInstance(result_update_date, tuple)
        self.assertIsInstance(result_update_date[0], dict)
        self.assertIsInstance(result_update_date[1], list)
        for result_item in result_update_date[1]:
            self.assertIsInstance(result_item, dict)

    def test_check_document_existance(self):
        check_false = app.check_document_existance('999999999999999999')
        check_true = app.check_document_existance(app.documents[0].get('number'))
        self.assertFalse(check_false)
        self.assertTrue(check_true)

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value=app.documents[len(app.documents) - 1].get('number')):
            name_end = app.get_doc_owner_name()
        self.assertEqual(name_end, app.documents[len(app.documents) - 1].get('name'))

    def test_get_all_doc_owners_names(self):
        all_doc_set = app.get_all_doc_owners_names()
        self.assertEqual(len(app.documents), len(all_doc_set))
        self.assertIsInstance(all_doc_set, set)
        for document in all_doc_set:
            self.assertIsInstance(document, str)

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf(app.documents[len(app.documents) - 1].get('number'))
        app.remove_doc_from_shelf(app.documents[len(app.documents) - 1].get('number'))

    def test_add_new_shelf(self):
        shelf_num = '999999'
        with patch('app.input', return_value=shelf_num):
            result_true = app.add_new_shelf()
        with patch('app.input', return_value=shelf_num):
            result_false = app.add_new_shelf()
        self.assertTrue(result_true[1])
        self.assertEqual(shelf_num, result_true[0])
        self.assertFalse(result_false[1])
        self.assertEqual(shelf_num, result_false[0])

    def test_append_doc_to_shelf(self):
        shelf_num = '999999'
        app.append_doc_to_shelf(app.documents[len(app.documents) - 1].get('number'), shelf_num)
        self.assertEqual(app.documents[len(app.documents) - 1].get('number'), app.directories.get(shelf_num)[0])

    def test_delete(self):
        for iter in range(len(app.documents)):
            with patch('app.input', return_value=app.documents[0].get('number')):
                app.delete_doc()
        docs_on_directories = 0
        for directory in app.directories.values():
            docs_on_directories += len(directory)
        self.assertEqual(docs_on_directories, 0)
        self.assertEqual(len(app.documents), 0)

    def test_get_doc_shelf(self):
        with patch('app.input', return_value=app.documents[len(app.documents) - 1].get('number')):
            shelf_num = app.get_doc_shelf()
        self.assertIsInstance(shelf_num, str)

    def test_move_doc_to_shelf(self):
        doc_num = app.documents[len(app.documents) - 1].get('number')
        break_flag = False
        doc_shelf = None
        for shelf, docs_on_shelf in app.directories.items():
            for document_num in docs_on_shelf:
                if doc_num == document_num:
                    doc_shelf = shelf
                    break_flag = True
                    break
            if break_flag:
                break
        self.assertEqual(app.directories.get(doc_shelf).count(doc_num), 1)
        shelf_num = '999999'
        with patch('app.input', side_effect=[doc_num, shelf_num]):
            app.move_doc_to_shelf()
        self.assertEqual(app.directories.get(shelf_num)[0], doc_num)
        self.assertEqual(app.directories.get(doc_shelf).count(doc_num), 0)

    def test_add_new_doc(self):
        self.assertIsNone(app.directories.get('999999'))
        count_doc_in = len(app.documents)
        with patch('app.input', side_effect=['9999999999', 'id card', 'Mickey Mouse', '999999']):
            app.add_new_doc()
        self.assertIsInstance(app.directories.get('999999'), list)
        self.assertEqual(count_doc_in+1, len(app.documents))


if __name__ == '__main__':
    unittest.main()