# crnlpanic.netsoc.co
crnlpanic.netsoc.co homepage and techtalks and other stuff - standalone version running on flask

i'm using this to do a demo dockerfile build for the docker talk

![demo image](https://raw.githubusercontent.com/crnbrdrck/crnlpanic.netsoc.co/master/demo.png?token=APL_mWJ_nXwuK0nxZdRcbPwpbirQyYehks5cSEo4wA%3D%3D)

## Adding talks
The index.py script automatically detects any techtalks in the `techtalks` directory and displays them, assuming the following;

- The techtalk directory has a `meta.json` file, which is a json file that must contain the following keys;
    - `title` for the title of the talk displayed over the image
    - `quote` for the italicized text displayed underneath the image
- The techtalk directory also has a `title.png` image, which will be displayed in the card
