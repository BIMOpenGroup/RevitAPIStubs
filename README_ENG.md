The repository code is based on [ironpython-stubs](https://github.com/gtalarico/ironpython-stubs).
I express my infinite gratitude to [gtalarico](https://github.com/gtalarico) for contributing to the development of the community of developers, scripts and plug-ins for engineering programs.
I did not fork his repository, because I want to make cardinal changes,
besides, the author has not been engaged in it for a long time, and a successor has not been found.

Just like in the base repository, "stubs" can be used in various text editors, but all examples will be covered in [visual studio code](https://code.visualstudio.com/).

In fact, the generated code cannot be called "stubs", but this name has already taken root in the community. If you want to learn about real stubs for python code, then read [here](https://mypy.readthedocs.io/en/stable/stubs.html).

## For users
Look for generated stubs in [releases](https://github.com/BIMOpenGroup/revitapistubs/releases).
As you can see, they are divided into `common` and `revit`.
`common` stores Windows system library stubs, IronPython packages, [Dynamo](https://github.com/DynamoDS) and [RPS](https://github.com/architecture-building-systems/revitpythonshell).
`revit` stores stubs for several versions of the `Revit API` libraries.
To avoid conflicts with the code analyzer, you need to connect stubs using two ways.
```json
// %APPDATA%\Code\User\settings.json
"python.analysis.extraPaths": [
    "YOUR_PATH\\stubs\\common",
    "YOUR_WAY\\stubs\\revit\\2019"
],
```

If you change the version of Revit for a particular project, you will have to repeat both paths.
```json
// .vscode/settings.json
"python.analysis.extraPaths": [
    "YOUR_PATH\\stubs\\common",
    "YOUR_WAY\\stubs\\revit\\2021"
],
```

Read more about connecting additional modules [here](https://code.visualstudio.com/docs/python/editing).
See examples of using stubs [here](https://github.com/BIMOpenGroup/RevitAPIStubs/tree/master/examples).

In order for the stubs to be as effective as possible, they must be finished by hand, but more on this in the examples.
Hopefully this will be fixed in the future.
If a new version of the Revit API is released, but the generation code does not change, then the archive of the latest release will be updated.

## For contributors
Any help is welcome!
Write questions, suggestions, comments. Even if I can't fix something in time, maybe someone from the community can help.

### General information
Stubs generation is possible via the console and this seems to be the preferred and flexible option, but for simplicity I chose [RevitPythonShell](https://github.com/architecture-building-systems/revitpythonshell).
For example, no need to take care of additional dependencies for `RevitAPIUI` or require a path to generate,
just open the Revit we need and run the script.
In addition, this repository is designed to generate stubs for Revit only.

Because `Pylance` is quite performant, unlike `Jedi`, stubs no longer need to be "minimized".
Therefore, it used to be necessary to run a script to process the generated stubs and form `stubs.min`.

I decided to place stubs in releases, because it makes no sense to store them in a repository.
The only reason to keep them in the repository is if someone will update/fix them by hand. But this is a very big and unnecessary work. It is better to try to improve the generator.

### How to generate stubs
In the RPS shell, run `src/main.py`, changing the path to `src_dir`.
If you run through a custom button on the RPS panel, then you don’t need to change anything in the code.
The stubs will be generated at the root of the repository.

### Rules
As in almost any open source, the [Forking Workflow] system is adopted here (https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).
Abstract:
- Making a fork of the repository;
- Create a branch from `master`;
- Make a `pull request` in `upstream/master`.

Branch naming rules:
- Kebab-case style;
- The first word is the fix/feature/refactor task, etc. Subsequent - a brief description, or issue number.
    fix-iss57 / feature-iss14 / refactor-generator.

Please add folders of various IDEs to your global gitignore.

### Current tasks
At the moment, the priority task is to improve the generator code.