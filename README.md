NBA cron
==========

Given a picture and a number *k*, this script outputs a version of your picture that only uses *k* colors. But it picks those *k* colors wisely (using the [k-Means Clustering](http://en.wikipedia.org/wiki/K-means_clustering) Algorithm) so as to preserve the original context of the image. You'd be amazed how much trendier you look with fewer colors. 

##How to run the script
1) **Get the file** entitled kMeansColor.py (can be done by downloading the zip file of this repo on github)

2) **Install dependencies**, of which there are two: [SciPy](http://www.scipy.org/install.html) and [PIL](http://www.pythonware.com/products/pil/#pil117) (Python Imaging Library). If you're a Mac-user you can install these by simply entering the following into the Terminal (you'll be prompted for your computer password):
```
sudo port install py27-scipy
sudo port install py27-pil
```

3) **Run the code** by entering the following into your terminal:
```
python2.7 kMeansPainting.py [filepath to picture] [number k]
```

Note that your terminal needs to be in the folder containing kMeansPainting.py; if this is not the case, then enter `cd [path to folder containing kMeansPainting.py]` before running the above line of code. 

When the script is complete, a new version of your image will appear containing only the most identifying *k* colors (it will NOT overwrite your original image). Most jpg/png files take ~2 seconds to complete, while high-resolution photos may take up to a minute (pending further testing).

4) **Report errors** that you encounter by letting me know (email: njn27@cornell.edu, twitter: @nikhilhyphen). I hacked this together quickly and haven't done much error handling or testing for corner cases, so if you let me know if run into issues I can update the code accordingly!


##Example
###Original vs. k=2:
![barca](http://i.imgur.com/GWUVRmB.jpg) ![barca2](http://i.imgur.com/m3yCu4n.png)

README

all files need to be full path
all gametimes are in Eastern Time
