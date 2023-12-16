## My workspace

添加Git说明与常用命令文档

Git概念添加常用命

gitUpdate.py


### Bash Profile

```
eval "$(/opt/homebrew/bin/brew shellenv)"

#enables colorin the terminal bash shell export
export CLICOLOR=1

#setsup thecolor scheme for list export
export LSCOLORS=gxfxcxdxbxegedabagacad

#sets up theprompt color (currently a green similar to linux terminal)
#export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;36m\]\w\[\033[00m\]\$'

#enables colorfor iTerm
export TERM=xterm-256color

#depot_tools
DEPOT_TOOLS_PATH=/Users/ruibin.chow/Documents/code/other_code/webrtc/gn
# export PATH="$DEPOT_TOOLS_PATH:$PATH"

export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export PATH="/opt/homebrew/opt/ruby@3.0/bin:$PATH"

alias python='python3'
alias pip='pip3'
# alias pod='arch -x86_64 pod'

alias cp='cp -ig'
alias mv='mv -ig'

export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles #ckbrew
eval $(/usr/local/Homebrew/bin/brew shellenv) #ckbrew

export HOMEBREW_NO_AUTO_UPDATE=true
alias brew-clean='brew cleanup --prune=all'
alias brew-cache='open /Users/ruibin.chow/Library/Caches/Homebrew'

XCODE_DERIVEDDATA=/Users/ruibin.chow/Library/Developer/Xcode/DerivedData
alias xcode-clean="du -sh $XCODE_DERIVEDDATA && rm -rf $XCODE_DERIVEDDATA/* && echo 'done.'"
alias xcode-size="du -sh $XCODE_DERIVEDDATA"
```

--- 

### QuickLook

* [quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins.git)
* [SourceCodeSyntaxHighlight](https://github.com/sbarex/SourceCodeSyntaxHighlight.git)

```
brew install qlcolorcode qlstephen qlmarkdown quicklook-json qlimagesize suspicious-package apparency quicklookase qlvideo
brew install webpquicklook
brew install --cask --no-quarantine syntax-highlight
```

---

### VS Code

#### Setting

```
// 将设置放入此文件中以覆盖默认设置
// https://blog.csdn.net/qq_35333978/article/details/121876103
{
    "editor.rulers": [80],
    "editor.wordWrap": "on",
    "editor.fontSize": 13.5,
    "editor.fontFamily": "Consolas, Menlo, Monaco, 'Courier New', monospace",
    "editor.guides.indentation": false,
    "editor.showDeprecated": false,
    "editor.fontLigatures": false,
    "editor.fontWeight": "normal",
    "editor.unicodeHighlight.ambiguousCharacters": false,
    "editor.scrollBeyondLastLine": false,

    "terminal.integrated.fontSize": 13,
    "terminal.integrated.fontWeightBold": "normal",
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.persistentSessionScrollback": 5000,
    "terminal.integrated.scrollback": 1000000,

    "window.newWindowDimensions": "inherit",
    // "window.commandCenter": true,
    "window.autoDetectColorScheme": true,

    "files.exclude": {
        "**/.DS_Store": true,
        "**/.git": true,
        "**/.hg": true,
        "**/.idea": true,
        "**/.svn": true,
        "**/*.pyc": true,
        "**/CVS": true,
        "**/tags": true
    },
    "files.autoSave": "afterDelay",

    "workbench.iconTheme": "material-icon-theme",
    "workbench.colorTheme": "Xcode 11 Default Light",
    "workbench.preferredDarkColorTheme": "Xcode 11 Default Dark",
    "workbench.preferredLightColorTheme": "Xcode 11 Default Light",
    "workbench.editorAssociations": {
        "*.card": "default",
        "*.plist": "default"
    },
    "workbench.tree.indent": 4,
    // "workbench.sideBar.location": "left",
    "workbench.startupEditor": "newUntitledFile",
    // "workbench.colorCustomizations": {
        // 编辑区域背景
        // "editor.background": "#2E2E2E",
        // // 侧边栏
        // "sideBar.background": "#2b2b2b",
        // "sideBar.foreground": "#999",
        // "sideBar.border": "#2b2b2b",
        // // 侧边栏列表
        // "list.inactiveSelectionBackground": "#32363d",
        // "list.inactiveSelectionForeground": "#dfdfdf",
        // "list.hoverBackground": "#32363d",
        // "list.hoverForeground": "#dfdfdf",
        // // peek 窗口
        // "peekView.border": "#5b99fc9c",
        // // 顶部 tab 栏
        // "tab.border": "#2e2e2e",
        // "tab.activeBackground": "#2e2e2e",
        // "tab.activeForeground": "#cfcfcf",
        // "tab.activeBorder": "#5b99fcb9",
        // "tab.hoverBackground": "#2e2e2e",
        // "tab.hoverBorder": "#5b99fcb9",
        // "tab.inactiveForeground": "#8e8e8e",
        // // 最左侧工具栏
        // "activityBar.background": "#ffffff",
        // // 状态栏
        // "statusBar.background": "#2a2a2a",
        // // panel 窗口
        // "panelTitle.activeBorder": "#5b99fc5b",
        // "panelTitle.activeForeground": "#cfcfcf",
        // // 光标
        // "editorCursor.foreground": "#7bfc5bb9",
        // // 当前行
        // "editor.lineHighlightBackground": "#32363d",
        // // 行号栏的当前行
        // "editorActiveLineNumber.activeForeground": "#9CA5B4",
        // // 行号
        // "editorLineNumber.foreground": "#777",
        // 标尺
        // "editorRuler.foreground": "#ff0000", 
        // // 快捷提示窗口
        // "editorSuggestWidget.highlightForeground": "#7bfc5ba2",
        // "editorSuggestWidget.selectedBackground": "#333f5c",
        // // 单击一个词时，其它相同单词
        // "editor.selectionHighlightBackground": "#ffe7921c",
        // "editor.selectionBackground": "#434e61c9",
        // // "editor.selectionHighlightBorder": "#90e97259",
        // // terminal 中的光标
        // "terminalCursor.foreground": "#7bfc5bb9",
        // // 侧边栏中一块区域的标题
        // "sideBarSectionHeader.background": "#32363d",
        // // 区域获取焦点时
        // "focusBorder": "#5b99fc36"
    // },
    "security.workspace.trust.untrustedFiles": "open",
    "update.mode": "none",

    "extensions.ignoreRecommendations": true,
    
    "remote.SSH.showLoginTerminal": true,
    "remote.SSH.connectTimeout": 45,
    
    // "C_Cpp.errorSquiggles": "Disabled",
    "C_Cpp.intelliSenseEngine": "disabled",
    "gitlens.hovers.currentLine.over": "line",
    "gitlens.currentLine.scrollable": false,
    "git.openRepositoryInParentFolders": "never",
    "gitlens.graph.minimap.enabled": false,
    
    "cmake.configureOnOpen": false,
    
    "search.useIgnoreFiles": false,
    "security.workspace.trust.banner": "never",
    "security.workspace.trust.enabled": false,
    "[javascript]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    
    //https://www.php.cn/faq/485739.html
    // "editor.tokenColorCustomizations": {
    //     "[Xcode 11 Default Light]": {
    //         "textMateRules": [
    //             {
    //                 "scope": "variable.parameter",
    //                 "settings": {
    //                     "foreground": "#00ff55",
    //                     "fontStyle": ""
    //                 }
    //             },
    //         ]
    //     }
    // }
}
```

#### Theme

* https://marketplace.visualstudio.com/items?itemName=arzg.xcode-theme
* https://marketplace.visualstudio.com/items?itemName=arc0re.theme-xcode-midnight

---

### Sublime Text

#### Settting

```
{
	"theme": "Default.sublime-theme",
	"color_scheme": "Packages/Colorsublime - Themes/Xcode_default.tmTheme",

	"open_files_in_new_window":false,
	"font_face": "Consolas",
	"font_size": 12,

	"tab_size": 4,
	"word_wrap": "true",
	"rulers": [80,80],
	"ignored_packages":
	[
		"Material Theme",
		"Vintage",
	],
}
```

#### Color

```
1.打开sublime text3，按“CTRL + `”切到控制台，输入

import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())

安装包管理器 。

2.需要安装Colorsublime插件

3.打开Package Control(CTRL +SHIFT+P)

输入install，然后点击Install Theme

搜索"Xcode default"
```

