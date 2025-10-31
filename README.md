# Careerist Test Automation repository
written in
### Python 3, Behave
https://www.careerist.com/automation


Browser Options set in Environment.py 
| Browser       | Headless  | Command                                      |
| ------------  | --------- | -------------------------------------------- |
| Chrome        | ❌        | `behave -D browser=chrome`                   |
| Chrome        | ✅        | `behave -D browser=chrome -D headless=true`  |
| Firefox       | ❌        | `behave -D browser=firefox`                  |
| Firefox       | ✅        | `behave -D browser=firefox -D headless=true` |
| BrowserStack  |           | `behave -D browser=browserstack`             |

