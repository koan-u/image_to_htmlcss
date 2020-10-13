BIT_SIZE = 2
SKIP_SIZE = 0

# HTML CONSTANTS
HTML_FORMAT_FIRST = [
    '<!DOCTYPE html>\n',
    '<html lang="en">\n',
    '  <head>\n',
    '    <meta charset="UTF-8">\n',
    '    <link rel="stylesheet" href="base.css">\n',
    '    <link rel="stylesheet" href="style.css">\n',
    '  </head>\n',
    '  <body>\n',
    '  <p class="bp"></p>\n',
]
DIV_FORMAT = '    <p class="p_{}_{}"></p>\n'
HTML_FORMAT_SECOND = [
    '  </body>\n',
    '</html>\n',
]

# CSS CONSTANTS
RESET_CSS = '* {margin: 0; padding: 0;}\n'
BASE_STYLE = 'p {{width: {}px; height: {}px; display: block; position: absolute;}}\n'
BASE_P_STYLE = '.bp {{width: {}px; height: {}px;}}\n'
STYLE_FORMAT = '.p_{}_{} {{ {} left: {}px; top: {}px;}}\n'
RGB_FORMAT = ' background-color: rgb({}, {}, {});'
