---
id: 1670
title: 'Scanning Documents: Lessons Learned'
date: 2009-11-27T10:00:21+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=1670
permalink: /scanning-documents-lessons-learned/
Image:
  - http://www.streamhead.com/wp-content/uploads/2009/11/autofeed_load.png
dsq_thread_id:
  - "48162104"
categories:
  - On Streamhead
---
<a title="Moving to paperless" href="http://www.streamhead.com/scanning-documents-step-moving-paperless-office/" target="_blank">In a bit of continuity</a>, I actually installed Ocropus and tried it out. Turns out, this really is beta software. There were a few too many loose nuts and bolts and I ended up going for a double headed VueScan and Evernote approach.

Ocropus itself takes bitmaps as input and does not do the actual scanning. For that, you need another tool. On Linux, <a title="XSane" href="http://www.xsane.org/" target="_blank">XSane</a> is pretty much the standard tool, which is also the one I used. And it turns out it&#8217;s also a good choice if you want to scan multiple pages. It will automatically scan a preset number of pages. You only need to make sure that you can place the page on your scanner before the scan begins (not always easy).

<div style="float:right;">
  <a title="analogue" href="http://www.flickr.com/photos/35135181@N06/3687559590/" target="_blank"><img src="http://farm3.static.flickr.com/2560/3687559590_eb47f2aa0d_m.jpg" border="0" alt="analogue" /></a><br /> <small><a title="Attribution-NonCommercial-ShareAlike License" href="http://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="Seán Venn" href="http://www.flickr.com/photos/35135181@N06/3687559590/" target="_blank">Seán Venn</a></small>
</div>

Based on a set of images, Ocropus starts its analysis. First it splits the documents in blocks and lines. Next is the Optical Character Recognition (OCR), which is where I got stuck. The OCR in Ocropus is based on an AI solution that needs to be trained. Sadly Ocropus came with incomplete or outdated recognition models. You can train Ocropus and create your own model, but for that you need a set of reference documents. You can imagine the time required to create the reference docs (there is a basic one available) and to train the algorithm.

It was too much for me, so I started looking for other solutions. I did stumble upon Cuneiform, but it didn&#8217;t seem to like my documents very much. The results were abysmal. As were any of the other programs I tried.

Eventually, I had a revelation. Evernote is not only my favorite note-keeping program, it also has OCR build in. And, from the few tests I did, pretty good one at that. So why not create a PDF, dump it in Evernote and let it do the OCR?

There are several ways to scan and create a PDF. You might want to check out the software that came with your scanner. <a title="iCopy" href="http://icopy.sourceforge.net/" target="_blank">iCopy</a> in combination with <a title="PDFCreator" href="http://www.pdfforge.org/" target="_blank">PDFCreator</a> is a good open source solution. And last but not least, if you want it really easy and don&#8217;t mind spending a fairly small amount of money, get yourself <a title="VueScan" href="http://www.hamrick.com/" target="_blank">VueScan</a>.

<div style="float:right;">
  <a title="MIni-DIY : Laptop Document Holder" href="http://www.flickr.com/photos/75761601@N00/4099472306/" target="_blank"><img src="http://farm3.static.flickr.com/2607/4099472306_5b35b17485_m.jpg" border="0" alt="MIni-DIY : Laptop Document Holder" /></a><br /> <small><a title="Attribution-NonCommercial License" href="http://creativecommons.org/licenses/by-nc/2.0/" target="_blank"><img src="http://www.streamhead.com/wp-content/plugins/photo-dropper/images/cc.png" border="0" alt="Creative Commons License" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a title="mskogly" href="http://www.flickr.com/photos/75761601@N00/4099472306/" target="_blank">mskogly</a></small>
</div>

Once you have a PDF, just move it into an Evernote note and if you are a premium subscriber, the OCR will kick in. If you aren&#8217;t a premium subscriber, there&#8217;s no OCR, but with a little tagging, you can at least very quickly retrieve the document. Something you weren&#8217;t able with the paper version. It&#8217;s already a big improvement.

Lessons learned:

  * Good document scanning, OCR and management isn&#8217;t easy. If you&#8217;re serious about it, some investment in good software and hardware will pay off big time.
  * If you&#8217;re going all the way with converting paper to digital, you need a dedicated scanner with automatic feeder. There really is no way around it. A flatbed scanner will only suffice if you are already digital and have only few documents arriving on paper. Which is very unlikely.
  * Most decent scanners will include some good software, which sort-of eliminates many of the issues discussed in this post. It does not solve the archiving though.

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->