This reference standard is generated using: https://github.com/innolitics/dicom-standard

## Updating the Standard

Clone the repository

    $ git clone git@github.com:innolitics/dicom-standard.git

Install the dependencies from requirements.txt

    $ cd dicom-standard
    $ pip install -r requirements.txt

Run the suggested commands from dicom-standard:

    $ make clean
    $ make updatestandard
    $ make

Finally, automatically extract the version:

    $ grep -m1 -oE 'DICOM PS3\.3 [0-9]{4}[a-z]' standard/part03.html | awk '{print "\"" $3 "\""}' > dist/version.json

Find the `./dist/*.json` files that were generated and copy it to the required location (`./dicom_standard` in this case).
