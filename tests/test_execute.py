from utils import execute as _execute


def test_execute():
    # language=javascript
    js_code = '''
              function sdk () {
                let sum = 0;
                for (const n of arguments) {
                  if (typeof n === "number") sum += n;
                }
                return sum;
              } \
              '''
    result = _execute.js.execute_javascript_by_execjs(js_code, func_name="sdk", func_args=(1, 2, "3"))
    print(result)

    # language=javascript
    js_code = '''
              function sdk () {
                let sum = 0;
                for (const n of arguments) {
                  if (typeof n === "number") sum += n;
                }
                return sum;
              } \
              '''
    result = _execute.js.execute_javascript_by_py_mini_racer(js_code, func_name="sdk", func_args=(1, 2, "3"))
    print(result)

    # language=javascript
    js_code = '''(function () {
      arguments = process.argv.slice(1).map(JSON.parse);
      let sum = 0;
      for (const n of arguments) {
        if (typeof n === "number") sum += n;
      }
      console.log(JSON.stringify({ "sum": sum }));
    })();'''

    result = _execute.js.execute_javascript_by_subprocess(js_code, arguments=(1, 2, "3",))
    print(result["sum"])


if __name__ == '__main__':
    test_execute()
