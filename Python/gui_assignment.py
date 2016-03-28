import wx

class guiClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(guiClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        menuBar = wx.MenuBar()

        #Main Menu
        fileButton = wx.Menu()
        editButton = wx.Menu()
        shellButton = wx.Menu()
        debugButton = wx.Menu()
        optionsButton = wx.Menu()
        windowButton = wx.Menu()
        helpButton = wx.Menu()

        #File Menu
        newFileButton = wx.Menu()
        openButton = wx.Menu()
        openModuleButton = wx.Menu()
        recentFilesButton = wx.Menu()
        classBrowserButton = wx.Menu()
        pathBrowserButton = wx.Menu()
        saveButton = wx.Menu()
        saveAsButton = wx.Menu()
        saveCopyAsButton = wx.Menu()
        printWindowButton = wx.Menu()
        closeButton = wx.Menu()
        exitButton = wx.Menu()

        #Edit Menu
        undoButton = wx.Menu()
        redoButton = wx.Menu()
        cutButton = wx.Menu()
        copyButton = wx.Menu()
        pasteButton = wx.Menu()
        selectAllButton = wx.Menu()
        findButton = wx.Menu()
        findAgainButton = wx.Menu()
        findSelectionButton = wx.Menu()
        findInFilesButton = wx.Menu()
        replaceButton = wx.Menu()
        goToLineButton = wx.Menu()
        showCompletionsButton = wx.Menu()
        expandWorldButton = wx.Menu()
        showCallTipButton = wx.Menu()
        showSurroundingParensButton = wx.Menu()
                
        #Shell Menu
        viewLastRestartButton = wx.Menu()
        restartShellButton = wx.Menu()

        #Debug Menu
        goToFileLineButton = wx.Menu()
        debuggerButton = wx.Menu()
        stackViewerButton = wx.Menu()
        autoOpenStackViewerButton = wx.Menu()

        #Options Menu
        configureIdleButton = wx.Menu()
        #Window Menu
        zoomHeightButton = wx.Menu()
        #Help Menu
        aboutIdleButton = wx.Menu()
        idleHelpButton = wx.Menu()
        pythonDocsButton = wx.Menu()
        

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        menuBar.Append(shellButton, 'Shell')
        menuBar.Append(debugButton, 'Debug')
        menuBar.Append(optionsButton, 'Options')
        menuBar.Append(windowButton, 'Window')
        menuBar.Append(helpButton, 'Help')

        fileButton.AppendMenu(wx.ID_ANY, 'New File', newFileButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Open', openButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Open Module', openModuleButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Recent Files', recentFilesButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Class Browser', classBrowserButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Path Browser', pathBrowserButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Save', saveButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Save As', saveAsButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Save Copy', saveCopyAsButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Print', printWindowButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Close', closeButton)
        fileButton.AppendMenu(wx.ID_ANY, 'Exit', exitButton)

        editButton.AppendMenu(wx.ID_ANY, 'Undo', undoButton)
        editButton.AppendMenu(wx.ID_ANY, 'Redo', redoButton)
        editButton.AppendMenu(wx.ID_ANY, 'Cut', cutButton)
        editButton.AppendMenu(wx.ID_ANY, 'Copy', copyButton)
        editButton.AppendMenu(wx.ID_ANY, 'Paste', pasteButton)
        editButton.AppendMenu(wx.ID_ANY, 'Select All', selectAllButton)
        editButton.AppendMenu(wx.ID_ANY, 'Find', findButton)
        editButton.AppendMenu(wx.ID_ANY, 'Find Again', findAgainButton)
        editButton.AppendMenu(wx.ID_ANY, 'Find Selection', findSelectionButton)
        editButton.AppendMenu(wx.ID_ANY, 'Find in Files', findInFilesButton)
        editButton.AppendMenu(wx.ID_ANY, 'Replace', replaceButton)
        editButton.AppendMenu(wx.ID_ANY, 'Go to Line', goToLineButton)
        editButton.AppendMenu(wx.ID_ANY, 'Show Completions', showCompletionsButton)
        editButton.AppendMenu(wx.ID_ANY, 'Expand World', expandWorldButton)
        editButton.AppendMenu(wx.ID_ANY, 'Show Call Tip', showCallTipButton)
        editButton.AppendMenu(wx.ID_ANY, 'Show Surrounding Parens', showSurroundingParensButton)

        shellButton.AppendMenu(wx.ID_ANY, 'View Last Restart', viewLastRestartButton)
        shellButton.AppendMenu(wx.ID_ANY, 'Restart Shell', restartShellButton)

        debugButton.AppendMenu(wx.ID_ANY, 'Go To File Line', goToFileLineButton)
        debugButton.AppendMenu(wx.ID_ANY, 'Debugger', debuggerButton)
        debugButton.AppendMenu(wx.ID_ANY, 'Stack Viewer', stackViewerButton)
        debugButton.AppendMenu(wx.ID_ANY, 'Auto Open Stack Viewer', autoOpenStackViewerButton)

        optionsButton.AppendMenu(wx.ID_ANY,'Configure Idle',configureIdleButton)

        windowButton.AppendMenu(wx.ID_ANY,'Zoom Height',zoomHeightButton)

        helpButton.AppendMenu(wx.ID_ANY,'Configure Idle',aboutIdleButton)
        helpButton.AppendMenu(wx.ID_ANY,'Idle Help',idleHelpButton)
        helpButton.AppendMenu(wx.ID_ANY,'Python Docs',pythonDocsButton)
        
        self.SetMenuBar(menuBar)

        wx.TextCtrl(panel, pos=(600, 3000), size=(600,3000))
        
        self.SetTitle('*Python 2.7.11 Shell*')
        self.Show(True)

    def Quit(self, e):
        self.Close()
    


def main():
    app = wx.App()
    guiClass(None)

    app.MainLoop()

main()
