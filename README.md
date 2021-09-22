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
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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

1. The reason I chose such an elaborate setup for such a seemingly simple app is because I realized that I could eventually use this as a replacement for Google images. It would allow for me to have better control over my own pictures, as well as a bigger storage space. As such, I built this setup with the intent to continue development past the scope of this internship application.

2. I built a multi-label neural network classifier for this app's image content recognition feature (it was more fun than just getting one off the internet). However, I grossly overestimated the capabilities of my computer when it came to training. Had to severely downsize just about everything. Even then, the performance is quite poor: 60% accuracy on 13 labels. 13 different classifiers, each handling one label, trained on specialized datasets, would likely yield far better results, but that's not really scallable. So, I kept the single model setup. I'm confident that, given time to obtain more computing power, I will enventually get it to where my overconfidence first thought it would go (decent accuracy at 600 labels). 

3. I left all the ML stuff in the shopifyChallenge/imageRepo/classifierScripts/ folder. 

4. If you want to try out the data processing scripts in there, here's where to download the data
4.1 https://github.com/cvdfoundation/open-images-dataset#download-images-with-bounding-boxes-annotations\
4.2 download the s3://open-images-dataset/tar/train_f.tar.gz one
4.3 get the labels from https://storage.googleapis.com/openimages/web/download_v4.html (the 600 label one)

USAGE INSTRUCTIONS:

These are rough instructions, to be updated, just in case you guys are that quick.

1. App should be loaded up with default pictures
2. You can choose a file in your computer by clicking on the big upload icon
3. You can now choose to either upload the image to the repo, by clicking upload
4. Or search for variations of that image in the repo by clicking search. This should update the listed pictures with the results, if any. Click on the big refresh go back.
6. Selecting a keyword in the dropdown should filter the pictures according to what the server thinks are in those pictures
7. Hovering over an image will reveal what the app thinks its contents is
8. The content filters person, man, building, tree work best. 



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
