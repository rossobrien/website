Title: Site Updates
date:   2013-11-10 11:30
author:   ross
category:   General
tags:   python, pelican, fabric, meta
slug:   site-updates

Recently I've been working on some changes to this site. The previous iteration of my website was custom built using a PHP framework called Kohana and the blog was run using Wordpress. I lost enthusiasm about finishing and maintaining the site, and I wasn't happy about how I had itegrated Wordpress. So I started looking around for alternative options.

After some consideration and experiments with various frameworks and content management systems, I settled on using <a href="http://docs.getpelican.com/en/3.3.0/" target="_blank">Pelican</a>, a Python static site generator. It allows me to write blog posts locally in Markdown, and all the maintenance is simple HTML and CSS that I can do quickly. The theme system is simple and easy to modify. 

I can deploy the static site using <a href="http://fabfile.org/‎" target="_blank">Fabric</a>, an awesome command-line tool for deploying to remote servers. I use Fabric in my daily work at <a href="http://pearup.com" target="_blank">Pear</a> to managing multiple development environments, so I was more than happy to find out the Pelican sets up a basic Fabric deploy script by default. After some minor modifications, I can regnerate and deploy my site in less than a minute.

In non-technical changes, I recently relocated to the Seattle area. I've always wanted to move out west, so when an opportunity come up to move out here, I jumped at the chance. I've started working remotely and will probably post about my thoughts on working from home in the near future. 

So that's all for now. I plan on posting here a little more frequently, so <a href="https://twitter.com/intent/user?screen_name=obrien_ross" target="_blank">follow me on Twitter</a> to stay up to date.