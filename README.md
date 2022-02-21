## My workspace

添加Git说明与常用命令文档

Git概念添加常用命

gitUpdate.py


### Bash Profile

```
#enables colorin the terminal bash shell export
export CLICOLOR=1

#setsup thecolor scheme for list export
export LSCOLORS=gxfxcxdxbxegedabagacad

#sets up theprompt color (currently a green similar to linux terminal)
#export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;36m\]\w\[\033[00m\]\$'

#enables colorfor iTerm
export TERM=xterm-256color

# depot_tools
DEPOT_TOOLS_PATH=/Users/ruibin.chow/Documents/code/other_code/webrtc
# CHROMIUM_BUILDTOOLS_PATH="$DEPOT_TOOLS_PATH/gn/buildtools"
# export CHROMIUM_BUILDTOOLS_PATH
export PATH=$PATH:$DEPOT_TOOLS_PATH/gn/depot_tools

export PATH=/usr/local/Cellar/protobuf/3.17.3/bin:$PATH

alias python='python3'
alias pip='pip3'
```

---

### VS Code

#### Setting

```
{
    "editor.fontFamily": "Consolas, Menlo, Monaco, 'Courier New', monospace",
    "files.autoSave": "afterDelay",
    "security.workspace.trust.untrustedFiles": "open",
    "editor.wordWrap": "on",
    "remote.SSH.showLoginTerminal": true,
    "remote.SSH.connectTimeout": 45,
    
    "editor.rulers": [
        80
    ],
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.fontSize": 13,
    "terminal.integrated.persistentSessionScrollback": 5000,
    "terminal.integrated.scrollback": 5000,
    "workbench.tree.indent": 4,
    "editor.minimap.enabled": false,
    "window.newWindowDimensions": "inherit",
    "workbench.colorTheme": "Xcode 11 Default Light",
    "workbench.list.keyboardNavigation": "filter", //按Cmd-Shift-E来获得Explorer焦点
    // "workbench.colorCustomizations": {
    //     "editorRuler.foreground":"#ff0000"
    //  },
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

