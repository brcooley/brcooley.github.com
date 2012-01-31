---
layout: default
title: GPG Key
date: 01/29/2012
---

## {{ page.title }} ##

As of {{ page.date }}, I have two public keys available.  For any released software which has a tag associated with the release, I sign the tag with my **[signing key][sk]**.  Generally, this key shouldn't be needed from here, as the project should contain instructions on verifying the tag, but for the paranoid, this serves as a seperate source of verification.

I also have a **[personal key][pk]** which can be used to encrypt email messages sent to me.  Below are the fingerprints for both keys.

### Key Fingerprints ###

{% include fingerprints.html %}

[sk]: signing.txt
[pk]: personal.txt