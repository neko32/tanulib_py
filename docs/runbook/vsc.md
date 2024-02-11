# Trouble shooting to set up Tanulib project in VSC

## Intellisense is not working after installing tlib package to pip

You may need to create .vscode at the root the project and create the below settings.json

```json
{
    "python.analysis.extraPaths": [
        "./tanukilib"
    ]
}
```
