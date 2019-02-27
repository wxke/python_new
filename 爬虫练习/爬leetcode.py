import requests
from bs4 import BeautifulSoup
url_login = 'https://leetcode-cn.com/accounts/login/'
s = requests.Session()


def login(url_login):
    res = s.get(url=url_login)
    csrf = res.headers['Set-Cookie'].split(';')[0].split("=")[1]
    data = {
               'csrfmiddlewaretoken': csrf,
               'login': '18645255095',
               'password': 'wxk1072650789',
               'next': '/problems',
    }
    headers_base = {
        'authority': 'leetcode-cn.com',
        'method': 'POST',
        'path': '/accounts/login/',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '528',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryrcsKr1InlE1EiFJW',
        'origin': 'https://leetcode-cn.com',
        'referer': 'https://leetcode-cn.com/accounts/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'x-csrftoken':csrf,
        'x-requested-with': 'XMLHttpRequest',
    }
    res = s.post(url=url_login, headers=headers_base, data=data)
    print(res.status_code)
    print(res.text)
    print(res.url)


if __name__ == '__main__':
    # q = {"form": {"fields": {"login": {"label": "\u8d26\u53f7", "value": "", "help_text": "", "errors": ["\u8be5\u5b57\u6bb5\u662f\u5fc5\u586b\u9879\u3002"], "widget": {"attrs": {"placeholder": "\u7528\u6237\u540d\u6216e-mail", "autofocus": "autofocus"}}}, "password": {"label": "\u5bc6\u7801", "value": "", "help_text": "", "errors": ["\u8be5\u5b57\u6bb5\u662f\u5fc5\u586b\u9879\u3002"], "widget": {"attrs": {"placeholder": "\u5bc6\u7801"}}}}, "field_order": ["login", "password"], "errors": []}, "html": "<!DOCTYPE html>\n\n\n<html>\n  <head>\n    <meta charset=\"utf-8\">\n    <title>Loading...</title>\n    <meta property=\"og:title\" content=\"\" />\n\n    \n    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover' name='viewport' />\n    \n    <meta name=\"description\" content=\"\u5907\u6218\u6280\u672f\u9762\u8bd5\uff1f\u529b\u6263\u63d0\u4f9b\u6d77\u91cf\u6280\u672f\u9762\u8bd5\u8d44\u6e90\uff0c\u5e2e\u52a9\u4f60\u9ad8\u6548\u63d0\u5347\u7f16\u7a0b\u6280\u80fd\uff0c\u8f7b\u677e\u62ff\u4e0b\u4e16\u754c IT \u540d\u4f01 Dream Offer\u3002\" />\n    \n    <meta name=\"keywords\" content=\"\u529b\u6263, \u529b\u6263\u4e2d\u56fd, LeetCode, lingkou, LC, LCCN, LeetCode\u4e2d\u56fd, LeetCode\u5b98\u7f51, \u9886\u6263, \u9886\u6263\u7f51, \u9886\u6263\u7f51\u7edc, \u9886\u6263\u4e2d\u56fd, \u5237\u9898, \u5728\u7ebf\u7f16\u7a0b, LeetCode\u9898\u5e93, \u9762\u7ecf, \u7b97\u6cd5, \u9762\u8bd5, \u9762\u8bd5\u9898, \u673a\u5668\u5b66\u4e60, \u5927\u6570\u636e, \u4ee3\u7801, \u6c47\u7f16, \u7f16\u7a0b, \u5f00\u53d1, \u7a0b\u5e8f\u5458, \u5de5\u7a0b\u5e08, \u7801\u519c, \u7a0b\u5e8f\u733f, BAT, BAT\u9762\u8bd5, OJ, online judge, coding , interview, \u6280\u672f\u9762\u8bd5, LeetCode\u4e2d\u6587\u7248, leetcodechina\" />\n    \n    <meta property=\"og:image\" content=\"https://static.leetcode-cn.com/cn-legacy-assets/images/LeetCode_Sharing.png\" />\n    <meta property=\"og:description\" content=\"\u5907\u6218\u6280\u672f\u9762\u8bd5\uff1f\u529b\u6263\u63d0\u4f9b\u6d77\u91cf\u6280\u672f\u9762\u8bd5\u8d44\u6e90\uff0c\u5e2e\u52a9\u4f60\u9ad8\u6548\u63d0\u5347\u7f16\u7a0b\u6280\u80fd\uff0c\u8f7b\u677e\u62ff\u4e0b\u4e16\u754c IT \u540d\u4f01 Dream Offer\u3002\" />\n\n    \n  \n  \n  <meta name=\"addon-sha\" content=\"\"/>\n  <meta name=\"addon-version\" content=\"\"/>\n  \n\n\n    <link rel=\"apple-touch-icon\" sizes=\"57x57\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-57x57.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"60x60\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-60x60.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"72x72\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-72x72.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"76x76\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-76x76.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"114x114\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-114x114.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"120x120\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-120x120.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"144x144\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-144x144.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"152x152\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-152x152.png\" />\n    <link rel=\"apple-touch-icon\" sizes=\"180x180\" href=\"https://static.leetcode-cn.com/cn-assets/icons/apple-touch-icon-180x180.png\" />\n    <link rel=\"icon\" type=\"image/png\" href=\"https://static.leetcode-cn.com/cn-assets/icons/favicon-16x16.png\" sizes=\"16x16\" />\n    <link rel=\"icon\" type=\"image/png\" href=\"https://static.leetcode-cn.com/cn-assets/icons/favicon-32x32.png\" sizes=\"32x32\" />\n    <link rel=\"icon\" type=\"image/png\" href=\"https://static.leetcode-cn.com/cn-assets/icons/favicon-96x96.png\" sizes=\"96x96\" />\n    <link rel=\"icon\" type=\"image/png\" href=\"https://static.leetcode-cn.com/cn-assets/icons/favicon-160x160.png\" sizes=\"160x160\" />\n    <link rel=\"icon\" type=\"image/png\" href=\"https://static.leetcode-cn.com/cn-assets/icons/favicon-192x192.png\" sizes=\"192x192\" />\n    <meta name=\"application-name\" content=\"LeetCode\"/>\n    <meta name=\"msapplication-TileColor\" content=\"#da532c\" />\n    <meta name=\"msapplication-TileImage\" content=\"/mstile-144x144.png\" />\n\n    \n      \n\n<script>\n  var match = document.cookie.match(/csrftoken=/g);\n  if (match.length >= 2) {\n    document.cookie = 'csrftoken=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/;';\n  }\n</script>\n\n    \n\n    <script>\n  var _hmt = _hmt || [];\n  (function() {\n    var hm = document.createElement(\"script\");\n    hm.src = \"https://hm.baidu.com/hm.js?fa218a3ff7179639febdb15e372f411c\";\n    var s = document.getElementsByTagName(\"script\")[0];\n    s.parentNode.insertBefore(hm, s);\n  })();\n</script>\n\n    \n\n\n<style>\n  #app {\n    height: 100%;\n    width: 100%;\n    overflow-y: auto;\n  }\n</style>\n\n    \n  </head>\n  <body>\n    \n<style id=\"initial-loading-style\">\n  #initial-loading {\n    position: fixed;\n    top: 0;\n    left: 0;\n    right: 0;\n    bottom: 0;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    background: white;\n    transition: opacity .6s;\n    z-index: 1;\n  }\n\n  #initial-loading[data-is-hide=\"true\"] {\n    opacity: 0;\n    pointer-events: none;\n  }\n\n  #initial-loading .spinner {\n    display: flex;\n  }\n\n  #initial-loading .bounce {\n    width: 18px;\n    height: 18px;\n    margin: 0 3px;\n    background-color: #999999;\n    border-radius: 100%;\n    display: inline-block;\n    -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;\n    animation: sk-bouncedelay 1.4s infinite ease-in-out both;\n  }\n\n  #initial-loading .bounce:nth-child(1) {\n    -webkit-animation-delay: -0.32s;\n    animation-delay: -0.32s;\n  }\n\n  #initial-loading .bounce:nth-child(2) {\n    -webkit-animation-delay: -0.16s;\n    animation-delay: -0.16s;\n  }\n\n  @-webkit-keyframes sk-bouncedelay {\n    0%, 80%, 100% {\n      -webkit-transform: scale(0);\n              transform: scale(0);\n    } 40% {\n      -webkit-transform: scale(1.0);\n              transform: scale(1.0);\n    }\n  }\n\n  @keyframes sk-bouncedelay {\n    0%, 80%, 100% {\n      -webkit-transform: scale(0);\n              transform: scale(0);\n    } 40% {\n      -webkit-transform: scale(1.0);\n              transform: scale(1.0);\n    }\n  }\n</style>\n\n<div id=\"initial-loading\">\n  <div class=\"spinner\">\n    <div class=\"bounce\"></div>\n    <div class=\"bounce\"></div>\n    <div class=\"bounce\"></div>\n  </div>\n</div>\n\n<div id=\"app\"></div>\n\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/runtime.6657f9406.js\" ></script>\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/common/global.8831d90ff.js\" ></script>\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/common/styles/index.17edee6ed.js\" ></script>\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/common/styles/new/index.0f0c7b4d6.js\" ></script>\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/vendor-libs.c12bc600e.js\" ></script>\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/common-libs.808524008.js\" ></script>\n    <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/new-libs.c563ac210.js\" ></script>\n\n    \n      <script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/locales/zh-Hans/index.118b8235e.js\" ></script>\n    \n\n    \n\n<script type=\"text/javascript\" src=\"https://static.leetcode-cn.com/cn-assets/webpack_bundles/new-apps/desktop.9de396bae.js\" ></script>\n\n\n\n    \n      <!-- \u767e\u5ea6\u8ba4\u8bc1 -->\r\n<!--\r\n<script type=\"text/javascript\">\r\n$(\"footer.site-footer .copyright a span\").html(\"Copyright \u00a9 2018 \u529b\u6263\u4fe1\u606f\u79d1\u6280\uff08\u4e0a\u6d77\uff09\u6709\u9650\u516c\u53f8\");\r\n</script>\r\n-->\r\n\r\n<style>\r\n.explore-card-base .explore-card .top-base .date-info{\r\n  opacity: 0;\r\n}\r\n</style>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n<!-- Global site tag (gtag.js) - Google Analytics -->\r\n<script async src=\"https://www.googletagmanager.com/gtag/js?id=UA-131851415-1\"></script>\r\n<script>\r\n  window.dataLayer = window.dataLayer || [];\r\n  function gtag(){dataLayer.push(arguments);}\r\n  gtag('js', new Date());\r\n\r\n  gtag('config', 'UA-131851415-1');\r\n</script>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n<!-- Start of KF5 supportbox script -->\r\n<script type=\"text/javascript\">\r\n  console.log(\"Support checking...\");\r\n\r\n  var currentURL = window.location.href;\r\n\r\n  function removeSurvey() {\r\n    localStorage.setItem(\"hideSurvey\", new Date().getTime());\r\n    document.querySelector(\".kf5-support-chat\").style.display = \"none\";\r\n  }\r\n\r\n  /* Load survey */\r\n  var isNewQuestionDetail =\r\n    currentURL.includes(\"/problems/\") &&\r\n    document.getElementById(\"question-detail-app\") == null;\r\n  var loadKF5Survey =\r\n    isNewQuestionDetail &&\r\n    (localStorage.getItem(\"hideSurvey\") == null ||\r\n      localStorage.getItem(\"hideSurvey\") <\r\n        new Date().getTime() - 1000 * 60 * 60 * 24 * 3);\r\n\r\n  if (loadKF5Survey) {\r\n    var src = '//assets-cdn.kf5.com/supportbox/main.js?' + new Date().getDay()\r\n    var script = document.createElement('script');\r\n    script.setAttribute('defer', '');\r\n    script.src = src;\r\n    script.onload = addCloseBtn;\r\n    script.onerror = loadError;\r\n    script.setAttribute('id', 'kf5-provide-supportBox');\r\n    script.setAttribute('kf5-domain', 'leetcode.kf5.com');\r\n    document.body.appendChild(script);\r\n    console.log(\"loading Support...\");\r\n  } else {\r\n    console.log(\"Support will not load.\");\r\n  }\r\n\r\n  // close script\r\n  function addCloseBtn() {\r\n    if (document.querySelector(\"#kf5-support-btn span\") == null) {\r\n      setTimeout(function() {\r\n        addCloseBtn();\r\n      }, 100);\r\n    } else {\r\n      console.log(\"Support loaded.\");\r\n      document.querySelector(\"#kf5-support-btn span\").innerHTML =\r\n        document.querySelector(\"#kf5-support-btn span\").innerHTML +\r\n        \" <span onclick='removeSurvey()' class='survey-close' title='\u5173\u95ed' style='font-size: 17px;line-height: 0px;margin-left: 5px'>\u00d7</span>\";\r\n    }\r\n  }\r\n\r\n  function loadError() {\r\n    console.log('Fail to load LeetCode Support.');\r\n  }\r\n</script>\r\n\r\n<style>\r\n  .survey-close:hover {\r\n    opacity: 0.6;\r\n  }\r\n  .kf5-chatSupport-left-bottom .kf5-chatSupport-style3,\r\n  .kf5-chatSupport-left-bottom .kf5-supportBox {\r\n    top: 0px !important;\r\n    bottom: auto !important;\r\n    right: 240px !important;\r\n    left: auto !important;\r\n  }\r\n\r\n  .kf5-chatSupport-style3::before {\r\n    margin-right: 0px !important;\r\n    font-size: 14px !important;\r\n    padding-right: 5px !important;\r\n  }\r\n\r\n  .kf5-chatSupport-style3 {\r\n    opacity: 0.85;\r\n    padding-right: 10px !important;\r\n    line-height: 33px !important;\r\n    font-size: 12px !important;\r\n    box-shadow: 0 0px 5px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);\r\n    border-radius: 0 0 5px 5px;\r\n  }\r\n</style>\r\n<!-- End of KF5 supportbox script -->\n    \n  </body>\n</html>\n"}
    # for k,v in q.items():
    #     print(k,v)
    # print(qq.encode().decode())
    login(url_login)