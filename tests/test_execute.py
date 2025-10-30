from utils import execute as _execute
from utils import logger as _logger


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

    logger = _logger.get_logger(__name__)
    _execute.cmd.execute_cmd_code_by_subprocess_popen("ping www.baidu.com", "cp936", logger)
    _execute.cmd.execute_cmd_code_by_subprocess_run("ping www.baidu.com", "cp936", logger)
    print(_execute.cmd.execute_cmd_code_by_subprocess_popen("pip show cwb-utils", "cp936", logger))
    print(_execute.cmd.execute_cmd_code_by_subprocess_popen("pip show frida", "cp936", logger))


if __name__ == '__main__':
    test_execute()
