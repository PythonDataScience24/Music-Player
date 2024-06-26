# Pylint

## Week 10 - Project part 3

4) Improve your code using pylint feedback (1 Points)
    * Fix at least 10 Messages
    * Add a "PYLINT.md" to your GitHub repository, containing the pylint output before fixing issues - where the issue that have been fixed are highlighted - and the new code fixing them

## Applied changes

Message: Unused variable 'index'
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/MusicDatabase.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "W0612:unused-variable",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/warning/unused-variable.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 4,
	"message": "Unused variable 'index'",
	"source": "Pylint",
	"startLineNumber": 153,
	"startColumn": 13,
	"endLineNumber": 153,
	"endColumn": 18
}]
Fix= delete the unused variable index

Message: Missing class docstring
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/Song.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0115:missing-class-docstring",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/missing-class-docstring.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Missing class docstring",
	"source": "Pylint",
	"startLineNumber": 35,
	"startColumn": 1,
	"endLineNumber": 35,
	"endColumn": 11
}]
Fix= added docstring

Message: standard import "import time" should be placed before "import sounddevice as sd"
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/Song.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0411:wrong-import-order",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/wrong-import-order.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "standard import \"import time\" should be placed before \"import sounddevice as sd\"",
	"source": "Pylint",
	"startLineNumber": 28,
	"startColumn": 1,
	"endLineNumber": 28,
	"endColumn": 12
}]
fix= reorder the imports and even remove some imports which i do not need anymore

Message: Line too long (120/100)
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/Song.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (120/100)",
	"source": "Pylint",
	"startLineNumber": 95,
	"startColumn": 1,
	"endLineNumber": 95,
	"endColumn": 1
}]
Fix= shorten the comment behind the line and place it above the according code line


Message: Variable name "originState" doesn't conform to snake_case naming style
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/dataframeManipulation.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0103:invalid-name",
		"target": {
			"$mid": 1,
			"external": "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/invalid-name.html",
			"path": "/en/latest/user_guide/messages/convention/invalid-name.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Variable name \"originState\" doesn't conform to snake_case naming style",
	"source": "Pylint",
	"startLineNumber": 13,
	"startColumn": 5,
	"endLineNumber": 13,
	"endColumn": 16
}]
Fix= change originState to origin_state

Message: Trailing whitespace
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/dataframeManipulation.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0303:trailing-whitespace",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/trailing-whitespace.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Trailing whitespace",
	"source": "Pylint",
	"startLineNumber": 40,
	"startColumn": 1,
	"endLineNumber": 40,
	"endColumn": 1
}]
Fix= delete the whitespace


Message: Final newline missing
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/dataframeManipulation.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0304:missing-final-newline",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/missing-final-newline.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Final newline missing",
	"source": "Pylint",
	"startLineNumber": 52,
	"startColumn": 1,
	"endLineNumber": 52,
	"endColumn": 1
}]
Fix= add newline

Message: Variable name "sortedDataframe" doesn't conform to snake_case naming style
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/dataframeManipulation.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0103:invalid-name",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/invalid-name.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Variable name \"sortedDataframe\" doesn't conform to snake_case naming style",
	"source": "Pylint",
	"startLineNumber": 31,
	"startColumn": 13,
	"endLineNumber": 31,
	"endColumn": 28
}]
Fix= change sortedDataframe to sorted_dataframe

Message: Line too long (109/100)
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/dataframeManipulation.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0301:line-too-long",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/line-too-long.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "Line too long (109/100)",
	"source": "Pylint",
	"startLineNumber": 4,
	"startColumn": 1,
	"endLineNumber": 4,
	"endColumn": 1
}]
Fix= add a newline to split up the text on 2 lines

Message: standard import "import csv" should be placed before "import pandas as pd"
Details:
[{
	"resource": "/Users/massimilianovella/Desktop/UNIVERSITÄT/Informatik/Semester 6/Programming for Data Science/Music-Player/MusicDatabase.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "C0411:wrong-import-order",
		"target": {
			"$mid": 1,
			"path": "/en/latest/user_guide/messages/convention/wrong-import-order.html",
			"scheme": "https",
			"authority": "pylint.readthedocs.io"
		}
	},
	"severity": 2,
	"message": "standard import \"import csv\" should be placed before \"import pandas as pd\"",
	"source": "Pylint",
	"startLineNumber": 2,
	"startColumn": 1,
	"endLineNumber": 2,
	"endColumn": 11
}]
Fix= switch around the imports so that import csv is before the pandas import


