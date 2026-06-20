# Resume Parser

A simple Resume Parser built using Python and PyPDF2.

## Features

* Extract Name from PDF resume
* Extract Email Address
* Extract Phone Number
* Extract Skills
* Extract Education Details
* User can provide any PDF resume path at runtime

## Technologies Used

* Python
* PyPDF2
* Regular Expressions (re)

## Installation

Install the required library:

```bash
pip install PyPDF2
```

## Usage

Run the program:

```bash
python main.py
```

Enter the PDF resume path when prompted:

```text
Enter Resume PDF Path: C:\Users\User\Downloads\resume.pdf
```

## Example Output

```text
===== RESUME DETAILS =====

Name: John Doe
Email: johndoe@gmail.com
Phone: 9876543210
Skills: ['Python', 'SQL']
Education: ['B.Tech']
```

## Future Improvements

* NLP-based skill extraction
* Multiple resume support
* CSV/Excel export
* Better name detection
* Advanced resume analytics

## Author

Raj Nishad
B.Tech CSE (Data Science)
