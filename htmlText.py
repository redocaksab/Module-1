def html(path, content):
    return fr'''
<!DOCTYPE html>
<html>
<head>
<title>Content</title>
<style>
    table {{
        border-collapse: collapse;
        border: 1px solid black;
     }}
     th, td {{
        border: 1px solid black;
     }}
   
</style>
</head>
<body>

<h1>{path}</h1>
</body>
<script>
    let arr = {content}
    if(typeof(arr[0]) != 'string') {{
    let table = document.createElement('table');
    let innerText = arr.map((item, index) => {{
        return `<tr>
            <td>${{item['name']}}</td>
            <td>${{item['size']}}</td>
            <td>${{item['hash']}}</td>
            <td>${{item['owner']}}</td>
            <td>${{item['time creation']}}</td>
            <td>${{item['time modification']}}</td>
          </tr>`
    }})
    let res = innerText.join('');
    table.innerHTML = `<th>name</th>
    <th>size</th>
    <th>hash</th>
    <th>owner</th>
    <th>time creation</th>
    <th>time modification</th>${{res}}
  </tr>`;
    document.body.append(table);
    }} else {{
          let arr = {content}
    let list = document.createElement('ol');
    let innerText = arr.map((item) => {{
        return `<li>${{item}}</li>`
    }})
    let res =  innerText.join("")
    list.innerHTML = res;
    document.body.append(list);
    }}

</script>
</html>
    '''
