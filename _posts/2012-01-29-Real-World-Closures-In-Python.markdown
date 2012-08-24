---
layout: post
title: Real World Closures in Python
desc: A mini-tutorial about scope and closures in Python, with production examples.
tags: [Python, Scope, Tutorials]
published: false
---

Closures in Python are one of those things that is really pretty basic when you understand them, but can be pretty difficult to wrap your head around, especially if you haven't dealt with strange things like [functional languages][hk].  Thankfully, this is the age of Google, and there are [many][0] [examples][1] of [explanations][2] out there, including [community-edited][3] ones.  I'll have to be honest and say those resources are how I first learned how to use closures, so by no means are they inadequate.  However, the one thing that probably bothers me the most about the current tutorials is that they skimp on the real-world examples.  Most computer science majors don't fully understand recursion until they see how it can be applied to real issues.  I know from a personal experience that [`fork()`][4] didn't make sense for some people until they realized what it did to a computer when placed inside an infinite loop.  So, this post is my attempt to correct this omission.  I'll go through what a closure is, how to use them, and I'll explain how


[hk]:http://www.haskell.org/
[0]:http://ynniv.com/blog/2007/08/closures-in-python.html
[1]:http://ivan.truemesh.com/archives/000392.html
[2]:https://gist.github.com/700292
[3]:http://stackoverflow.com/q/233673/950912
[4]:http://pubs.opengroup.org/onlinepubs/009695399/functions/fork.html