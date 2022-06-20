import unittest
import os
from task1 import LS
from task1 import Path_Mode
from task1 import Time_Mode


class TestLS(unittest.TestCase):
    def setUp(self):
      self.script_path = '/home/sashap/python'
      self.content_list = ['content.txt', 'htmlText.py', 'content.json', 'test.html', '__pycache__', 'content.csv', 'tests', 'task1.py', 'content.html', 'test.py', 'get-pip.py', 'UnitTest.py']
      self.file_list = ['/home/sashap/python/content.txt', '/home/sashap/python/htmlText.py', '/home/sashap/python/content.json', '/home/sashap/python/test.html', '/home/sashap/python/content.csv', '/home/sashap/python/task1.py', '/home/sashap/python/content.html', '/home/sashap/python/test.py', '/home/sashap/python/get-pip.py', '/home/sashap/python/UnitTest.py']
      self.dir_list = ['/home/sashap/python/__pycache__', '/home/sashap/python/tests']
      self.file_path = '/home/sashap/python/htmlText.py'
      self.file_info = {'name': '/home/sashap/python/htmlText.py', 'size': 1308, 'hash': 'e6861b91cc7dd46b7fca5b502f656661', 'owner': 'sashap', 'time creation': 1655485285.674956, 'time modification': 1655485285.674956}
      self.dir_path = '/home/sashap/python/tests'
      self.dir_info = {'name': '/home/sashap/python/tests', 'size': 4096, 'hash': '4dede231df0158ca1a6ff8686e88f644', 'owner': 'sashap', 'time creation': '2022-06-17 15:40:34', 'time modification': '2022-06-17 06:31:05'}

      self.txt_path = os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.txt')
      self.json_path = os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.json')
      self.csv_path = os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.csv')
      self.html_path = os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.html')

      self.txt_content = str([{'name': '/home/sashap/python/htmlText.py', 'size': 1308, 'hash': 'e6861b91cc7dd46b7fca5b502f656661', 'owner': 'sashap', 'time creation': 1655485285.674956, 'time modification': 1655485285.674956}, {'name': '/home/sashap/python/test.html', 'size': 644, 'hash': '27c190525132a03d6d4285ea615d3af2', 'owner': 'sashap', 'time creation': 1655400852.583717, 'time modification': 1655400852.583717}, {'name': '/home/sashap/python/task1.py', 'size': 7288, 'hash': '67ef67644bf04b006c0e07f78348f7a9', 'owner': 'sashap', 'time creation': 1655481483.7449908, 'time modification': 1655481483.7449908}, {'name': '/home/sashap/python/test.py', 'size': 153, 'hash': '9a66ad517d769c3a423352e22d8eb433', 'owner': 'sashap', 'time creation': 1655396154.3637412, 'time modification': 1655396154.3637412}, {'name': '/home/sashap/python/get-pip.py', 'size': 2680354, 'hash': '4b05a6c5742ffff285917b2d4cb3884b', 'owner': 'sashap', 'time creation': 1655368107.6838846, 'time modification': 1655368107.6838846}, {'name': '/home/sashap/python/UnitTest.py', 'size': 6276, 'hash': 'b9ce3999fc07df8e79038e0cc7137884', 'owner': 'sashap', 'time creation': 1655486472.8449452, 'time modification': 1655486472.8449452}])
      self.csv_content = '''name,size,hash,owner,time creation,time modification
/home/sashap/python/content.txt,1187,03ab749d95ede7f12050b67401c735a9,root,1655486745.9349427,1655486745.9349427
/home/sashap/python/htmlText.py,1308,e6861b91cc7dd46b7fca5b502f656661,sashap,1655485285.674956,1655485285.674956
/home/sashap/python/content.json,1385,0ad4e8b3528d5eb01d6dc839aff117dc,root,1655486750.4849427,1655486750.4849427
/home/sashap/python/test.html,644,27c190525132a03d6d4285ea615d3af2,sashap,1655400852.583717,1655400852.583717
/home/sashap/python/task1.py,7288,67ef67644bf04b006c0e07f78348f7a9,sashap,1655481483.7449908,1655481483.7449908
/home/sashap/python/content.html,4411,2aae9953636d7363d87e403ae54f2987,root,1655486759.7249424,1655486759.7249424
/home/sashap/python/test.py,153,9a66ad517d769c3a423352e22d8eb433,sashap,1655396154.3637412,1655396154.3637412
/home/sashap/python/get-pip.py,2680354,4b05a6c5742ffff285917b2d4cb3884b,sashap,1655368107.6838846,1655368107.6838846
/home/sashap/python/UnitTest.py,6276,b9ce3999fc07df8e79038e0cc7137884,sashap,1655486472.8449452,1655486472.8449452
'''
      json_content = str([{"name": "/home/sashap/python/content.txt", "size": 1187, "hash": "03ab749d95ede7f12050b67401c735a9", "owner": "root", "time creation": 1655486745.9349427, "time modification": 1655486745.9349427}, {"name": "/home/sashap/python/htmlText.py", "size": 1308, "hash": "e6861b91cc7dd46b7fca5b502f656661", "owner": "sashap", "time creation": 1655485285.674956, "time modification": 1655485285.674956}, {"name": "/home/sashap/python/test.html", "size": 644, "hash": "27c190525132a03d6d4285ea615d3af2", "owner": "sashap", "time creation": 1655400852.583717, "time modification": 1655400852.583717}, {"name": "/home/sashap/python/task1.py", "size": 7288, "hash": "67ef67644bf04b006c0e07f78348f7a9", "owner": "sashap", "time creation": 1655481483.7449908, "time modification": 1655481483.7449908}, {"name": "/home/sashap/python/test.py", "size": 153, "hash": "9a66ad517d769c3a423352e22d8eb433", "owner": "sashap", "time creation": 1655396154.3637412, "time modification": 1655396154.3637412}, {"name": "/home/sashap/python/get-pip.py", "size": 2680354, "hash": "4b05a6c5742ffff285917b2d4cb3884b", "owner": "sashap", "time creation": 1655368107.6838846, "time modification": 1655368107.6838846}, {"name": "/home/sashap/python/UnitTest.py", "size": 6276, "hash": "b9ce3999fc07df8e79038e0cc7137884", "owner": "sashap", "time creation": 1655486472.8449452, "time modification": 1655486472.8449452}])
      self.json_content = json_content.replace("'", '''"''')
      self.html_content = '''
<!DOCTYPE html>
<html>
<head>
<title>Content</title>
<style>
    table {
        border-collapse: collapse;
        border: 1px solid black;
     }
     th, td {
        border: 1px solid black;
     }
   
</style>
</head>
<body>

<h1>/home/sashap/python/content.html</h1>
</body>
<script>
    let arr = [{'name': '/home/sashap/python/content.txt', 'size': 1187, 'hash': '03ab749d95ede7f12050b67401c735a9', 'owner': 'root', 'time creation': 1655486745.9349427, 'time modification': 1655486745.9349427}, {'name': '/home/sashap/python/htmlText.py', 'size': 1308, 'hash': 'e6861b91cc7dd46b7fca5b502f656661', 'owner': 'sashap', 'time creation': 1655485285.674956, 'time modification': 1655485285.674956}, {'name': '/home/sashap/python/content.json', 'size': 1385, 'hash': '0ad4e8b3528d5eb01d6dc839aff117dc', 'owner': 'root', 'time creation': 1655486750.4849427, 'time modification': 1655486750.4849427}, {'name': '/home/sashap/python/test.html', 'size': 644, 'hash': '27c190525132a03d6d4285ea615d3af2', 'owner': 'sashap', 'time creation': 1655400852.583717, 'time modification': 1655400852.583717}, {'name': '/home/sashap/python/task1.py', 'size': 7288, 'hash': '67ef67644bf04b006c0e07f78348f7a9', 'owner': 'sashap', 'time creation': 1655481483.7449908, 'time modification': 1655481483.7449908}, {'name': '/home/sashap/python/test.py', 'size': 153, 'hash': '9a66ad517d769c3a423352e22d8eb433', 'owner': 'sashap', 'time creation': 1655396154.3637412, 'time modification': 1655396154.3637412}, {'name': '/home/sashap/python/get-pip.py', 'size': 2680354, 'hash': '4b05a6c5742ffff285917b2d4cb3884b', 'owner': 'sashap', 'time creation': 1655368107.6838846, 'time modification': 1655368107.6838846}, {'name': '/home/sashap/python/UnitTest.py', 'size': 6276, 'hash': 'b9ce3999fc07df8e79038e0cc7137884', 'owner': 'sashap', 'time creation': 1655486472.8449452, 'time modification': 1655486472.8449452}]
    if(typeof(arr[0]) != 'string') {
    let table = document.createElement('table');
    let innerText = arr.map((item, index) => {
        return `<tr>
            <td>${item['name']}</td>
            <td>${item['size']}</td>
            <td>${item['hash']}</td>
            <td>${item['owner']}</td>
            <td>${item['time creation']}</td>
            <td>${item['time modification']}</td>
          </tr>`
    })
    let res = innerText.join('');
    table.innerHTML = `<th>name</th>
    <th>size</th>
    <th>hash</th>
    <th>owner</th>
    <th>time creation</th>
    <th>time modification</th>${res}
  </tr>`;
    document.body.append(table);
    } else {
          let arr = [{'name': '/home/sashap/python/content.txt', 'size': 1187, 'hash': '03ab749d95ede7f12050b67401c735a9', 'owner': 'root', 'time creation': 1655486745.9349427, 'time modification': 1655486745.9349427}, {'name': '/home/sashap/python/htmlText.py', 'size': 1308, 'hash': 'e6861b91cc7dd46b7fca5b502f656661', 'owner': 'sashap', 'time creation': 1655485285.674956, 'time modification': 1655485285.674956}, {'name': '/home/sashap/python/content.json', 'size': 1385, 'hash': '0ad4e8b3528d5eb01d6dc839aff117dc', 'owner': 'root', 'time creation': 1655486750.4849427, 'time modification': 1655486750.4849427}, {'name': '/home/sashap/python/test.html', 'size': 644, 'hash': '27c190525132a03d6d4285ea615d3af2', 'owner': 'sashap', 'time creation': 1655400852.583717, 'time modification': 1655400852.583717}, {'name': '/home/sashap/python/task1.py', 'size': 7288, 'hash': '67ef67644bf04b006c0e07f78348f7a9', 'owner': 'sashap', 'time creation': 1655481483.7449908, 'time modification': 1655481483.7449908}, {'name': '/home/sashap/python/test.py', 'size': 153, 'hash': '9a66ad517d769c3a423352e22d8eb433', 'owner': 'sashap', 'time creation': 1655396154.3637412, 'time modification': 1655396154.3637412}, {'name': '/home/sashap/python/get-pip.py', 'size': 2680354, 'hash': '4b05a6c5742ffff285917b2d4cb3884b', 'owner': 'sashap', 'time creation': 1655368107.6838846, 'time modification': 1655368107.6838846}, {'name': '/home/sashap/python/UnitTest.py', 'size': 6276, 'hash': 'b9ce3999fc07df8e79038e0cc7137884', 'owner': 'sashap', 'time creation': 1655486472.8449452, 'time modification': 1655486472.8449452}]
    let list = document.createElement('ol');
    let innerText = arr.map((item) => {
        return `<li>${item}</li>`
    })
    let res =  innerText.join("")
    list.innerHTML = res;
    document.body.append(list);
    }

</script>
</html>
    '''

    def test_get_path(self):
        self.assertEqual(LS.get_path(Path_Mode.SCRIPT_PATH), self.script_path)

    def test_get_content_list(self):
        self.assertListEqual(LS.get_content_list(self.script_path), self.content_list)

    def test_get_file_list(self):
        self.assertListEqual(LS.get_file_list(self.script_path), self.file_list)

    def test_get_directory_list(self):
        self.assertListEqual(LS.get_directory_list(self.script_path), self.dir_list)

    def test_get_file_info(self):
        self.assertDictEqual(LS.get_file_info(self.file_path, Time_Mode.UNIX), self.file_info)

    def test_get_directory_info(self):
        self.assertDictEqual(LS.get_directory_info(self.dir_path, Time_Mode.UTC), self.dir_info)

    def test_save_as_txt(self):
        with open(self.txt_path, "r") as txtfile:
           content = txtfile.read()
        self.assertEqual(content, self.txt_content)

    def test_save_as_csv(self):
        with open(self.csv_path, "r") as csvfile:
           content = csvfile.read()
        self.assertEqual(content, self.csv_content)

    def test_save_as_json(self):
        with open(self.json_path, "r") as jsonfile:
           content = jsonfile.read()
        self.assertEqual(content, self.json_content)

    def test_save_as_html(self):
        with open(self.html_path, "r") as htmlfile:
           content = htmlfile.read()
        self.assertEqual(content, self.html_content)

unittest.main()
    

    