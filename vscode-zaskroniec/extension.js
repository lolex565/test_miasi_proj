const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

function activate(context) {
  const disposable = vscode.commands.registerCommand('zaskroniec.runFile', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage('Brak aktywnego pliku do uruchomienia.');
      return;
    }

    if (path.extname(editor.document.uri.fsPath) !== '.zas') {
      vscode.window.showErrorMessage('Uruchamianie dostępne tylko dla plików .zas.');
      return;
    }

    await editor.document.save();

    const workspaceFolder = vscode.workspace.getWorkspaceFolder(editor.document.uri);
    if (!workspaceFolder) {
      vscode.window.showErrorMessage('Plik musi znajdować się w otwartym folderze workspace.');
      return;
    }

    const workspacePath = workspaceFolder.uri.fsPath;
    const transpilerPath = path.join(workspacePath, 'zaskroniec.py');
    if (!fs.existsSync(transpilerPath)) {
      vscode.window.showErrorMessage('Nie znaleziono pliku zaskroniec.py w katalogu workspace.');
      return;
    }

    const terminal = vscode.window.createTerminal({
      name: 'Zaskroniec',
      cwd: workspacePath
    });

    const filePath = editor.document.uri.fsPath;
    terminal.show(true);
    terminal.sendText(`python "${transpilerPath}" "${filePath}"`);
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
