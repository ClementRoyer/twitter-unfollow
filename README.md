<h1 align="center">
  Twitter-unfollow
  <br>
</h1>

<h4 align="center">Send you a DM when you lose a follower</h4>


<br>

<div align="center">

[![License][license-img]][license] &nbsp; [![Profile][profile-img]][profile]


<!-- TOC -->
<p align="center">
  <a href="#install">Install</a> &nbsp; • &nbsp;
  <a href="#schedule">Schedule</a>
</p>

<!-- omit in toc -->
## 

</div>


## Install

1) `git clone git@github.com:ClementRoyer/twitter-unfollow.git`
2) `cd twitter-unfollow`
3) `pip3 install -r requirements.txt`
4) Update tokens in `main.py`
5) `python3 main.py`


## Schedule

1) `sudo crontab -e`
2) Add `0 12 1 * * /usr/bin/python3 {path to the repo}/main.py >/dev/null 2>&1`
3) This will run once a month.
<!-- footer -->

<!-- omit in toc -->
#

<div align="center"> 
  <sub>Built with ❤︎ by
  <a href="https://www.linkedin.com/in/cl%C3%A9ment-royer/">Clément ROYER</a> 
<br><br>

[![0](https://img.shields.io/badge/Usage_Policy-black.svg?style=flat&logo=Markdown&logoColor=white&labelColor=black&color=black)][license] [![0](https://img.shields.io/badge/Clément_royer-black.svg?style=flat&logo=Linkedin&labelColor=black&color=black)][Linkedin] ![visitors](https://visitor-badge.glitch.me/badge?page_id=clementroyer_twitter-unfollow----tag)
</div>

<!-- omit in toc -->
# 

<!-- links -->
[linkedin]: https://www.linkedin.com/in/cl%C3%A9ment-royer/
[license]: ./LICENSE
[changelog]: ./changelog
[documentation]: .
[profile]: https://github.com/ClementRoyer


<!-- Images -->
[changelog-img]: https://img.shields.io/badge/Changelog-black.svg?&style=for-the-badge&logo=Markdown&logoColor=white
[profile-img]: https://img.shields.io/badge/my_profile-black.svg?&style=for-the-badge&logo=github&logoColor=white
[license-img]: https://img.shields.io/badge/license-black.svg?&style=for-the-badge&logo=Markdown&logoColor=white
[documentation-img]: https://img.shields.io/badge/documentation-black.svg?&style=for-the-badge&logo=mail.ru&logoColor=white