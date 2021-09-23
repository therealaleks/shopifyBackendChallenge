<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/therealaleks/shopifyBackendChallenge">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Simple Image Repo</h3>

  <p align="center">
    A submission for Shopify's Winter 2022 Challenge
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![SIR Screen Shot](images/screenshot.png)

### A few things...

1. The reason I chose such an elaborate setup for such a seemingly simple app is because I realized that I could eventually use this as a replacement for Google images. It would allow for increased privacy, as well as a bigger storage space. I plan on developing it much further.

2. I trained a multi-label neural network classifier for this app's image content recognition feature (it was more fun than just getting one off the internet). However, I grossly overestimated the capacity of my computer when it came to training. Had to severely downsize just about everything. I went from 600 labels to 13 labels. Ironically, the dataset for 600 became unfit for 13. It was a huuge time sink and the performance is still quite poor: 60% accuracy on 13 labels. 13 different classifiers, each handling one label, trained on specialized datasets, would likely yield far better results, but that's not really scallable. So, I kept the single model setup. I'm confident that, given time to obtain more computing power, I will enventually get it to where my overconfidence first thought it would go (decent accuracy at 600 labels). 

3. I left all the ML stuff in the shopifyChallenge/imageRepo/classifierScripts/ folder. If you want to try out the data processing scripts in there, here's where to download the data
    https://github.com/cvdfoundation/open-images-dataset#download-images-with-bounding-boxes-annotations\
    (download the s3://open-images-dataset/tar/train_f.tar.gz one)
    Then get the labels from https://storage.googleapis.com/openimages/web/download_v4.html (the 600 label one)
    
4. I didn't really see the point of search based on filename or given title. Who remembers the file names of their pictures?

USAGE INSTRUCTIONS:

1. App should be loaded up with default pictures
2. You can choose a file in your computer by clicking on the big upload icon
3. You can now choose to either upload the image to the repo, by clicking upload
4. Or search for variations of that image in the repo by clicking search. This should update the listed pictures with the results, if any. Click on the big refresh to start over.
6. Selecting a keyword in the dropdown should filter the pictures according to what the server thinks are in those pictures
7. Hovering over an image will reveal what the app thinks its contents is
8. The content filters person, man, building, tree work best. 

RELEVANT TESTS (More specific expected behavior):

1. Make sure a file can be selected, or swapped out for another file.
2. If there are variations of that picture already in the repo (different dimensions, subtle transparent watermark etc), clicking on search should return those instances.
3. Clicking on upload should upload the picture to the repo and update the listed images right away. 
4. Upon hovering over listed uploaded pictures, check that there's a half-decent (and I do mean half) attempt at recognizing the contents
5. Clicking on an image should bring you to the image's URL
6. Refreshing should always bring back the complete set of images.
7. Selecting keywords in the dropdown should instantly filter out the images whose contents (determined by the server) don't fit the keywords. (It's a highly imperfect feature. As mentionned earlier, it works best with the keywords Person, Tree, Building, man.

PLANNED FEATURES:
1. Infinite scrolling so we don't load all the pictures at once
2. Filtering on resolution. The image dimensions are already stored in the database.
3. Improved image content recognition
4. Improved security (password and server authentication)
5. Implementing typescript to the React code
6. Adding image compression
7. Also allow videos
8. Video recognition
9. Perhaps a prettier UI
10. Routing on the clientside

### Built With

* [ReactJs](https://reactjs.org/)
* [Django](https://www.djangoproject.com/)
* [Node.Js](https://nodejs.org/en/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* node 14.15.1
* yarn 1.22.10
* Python 3.9.7

### Installation

First clone the repo and get into the shopifyBackendChallenge/ directory (the same one as this readme)

1. Start server and install server dependencies
   ```sh
   ./startServer.sh
   ```
2. Start client and install client dependencies
   ```sh
   ./startClient.sh
   ```




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
