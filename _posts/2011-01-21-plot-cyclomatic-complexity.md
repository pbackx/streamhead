---
id: 2988
title: How to Plot the Cyclomatic Complexity of Your Project
date: 2011-01-21T16:00:17+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2988
permalink: /plot-cyclomatic-complexity/
dsq_thread_id:
  - "213442529"
image: /wp-content/uploads/2011/01/complexity.png
categories:
  - Java and JavaScript
---
The Cyclomatic Complexity Number of your program is a very rough measurement of how many paths can be taken through your source code. It can be calculated fully automatically. While it is far from perfect, it will give you an idea of how complex your program is. More importantly, it can also be used as a metric for the complexity evolution of a program over time. This post shows how to create this graph using some basic tools.

<!--more-->

One of my preferred talks at Devoxx 2010 was Neal Ford&#8217;s explanation of how the design of a program emerges over time. You can <a title="Implementing Emergent Design" href="http://www.parleys.com/d/2165" target="_blank">watch the Implementing Emergent Design talk on Parleys</a> (it&#8217;s not free for now, but should be within a few months) or <a title="Neal Ford - Emergent Design And Evolutionary Architecture" href="http://www.slideshare.net/ThoughtWorks/neal-ford-emergent-design-and-evolutionary-architecture" target="_blank">view slides from a similar, but longer, talk</a> he held at another time and place. <a title="Neal Ford on Emergent Design at IBM developerWorks" href="http://bit.ly/nf-ead-all" target="_blank">Most interesting is however his series of articles on IBM&#8217;s developerWorks</a>. It goes in-depth on all the materials presented in the slides. Very very highly recommended.

Design can emerge when you refactor code to extract patterns or design elements from existing code. But at what point do you refactor and why? The goal of most (all?) refactoring is to reduce code complexity, which can be measured up to a certain point. <a title="Cyclomatic complexity on Wikipedia" href="http://en.wikipedia.org/wiki/Cyclomatic_complexity" target="_blank">Cyclomatic complexity</a> is one such measurement.

For part of a project I&#8217;m working on the graph looks like this (click for full size):

[<img class="alignnone size-medium wp-image-2989" title="cyclomatic_complexity_number_example" src="http://www.streamhead.com/wp-content/uploads/2011/01/cyclomatic_complexity_number_example-300x140.png" alt="" width="300" height="140" srcset="http://www.streamhead.com/wp-content/uploads/2011/01/cyclomatic_complexity_number_example-300x140.png 300w, http://www.streamhead.com/wp-content/uploads/2011/01/cyclomatic_complexity_number_example-1024x477.png 1024w, http://www.streamhead.com/wp-content/uploads/2011/01/cyclomatic_complexity_number_example.png 1217w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.streamhead.com/wp-content/uploads/2011/01/cyclomatic_complexity_number_example.png)

On the X axis are the Subversion revision numbers. The initial check-in of this particular bit of code was around revision 20000, hence that&#8217;s where the graph starts.

The Y axis shows:

  * in green (left axis) the sum of the cyclomatic complexity of each method in the program. You can clearly see it rise as additional features are added. It never decreases, which could be a cause for concern.
  * in red (right axis) the average of the cyclomatic complexity per method. This is fairly constant which is good. It should be noted that getters and setters influence this metric (they are all counted and have a CCN of 1) . So I&#8217;m not sure how valuable the average is for Java code.
  * blue (right axis) shows the average number of actual code lines per method. Again this is fairly small so I think we might need to adapt the calculations to not take into account some of the basic glue code that we use so often in Java (getters, setters, builders)

In hindsight, I wish I would&#8217;ve used date labels instead of revisions, but the graph shows a good year of development time. In that year the code complexity almost quadrupled! Which will undoubtedly also affect maintenance costs and the number of bugs.

## How to Create Your Own Cyclomatic Complexity Plot

I&#8217;d been holding off on trying this out since Devoxx (mid November last year) because I thought it would be complicated and time-consuming. But it turns out that wasn&#8217;t true at all. Creating the basic scripts I&#8217;ll show you here only took me an hour. Executing them was another hour. Keep in mind, that those scripts aren&#8217;t very advanced, fault tolerant or configurable. I invite any participation and expansion.

What you&#8217;ll need to get started:

  * A command line client for your version control system. In my case I used <a title="CollabNet Subversion command line client" href="http://www.collab.net/downloads/subversion/" target="_blank">the CollabNet Subversion Command-Line Client</a> which was already on my system.
  * Some way to calculate the cyclomatic complexity number (CCN) of your code. <a title="JavaNCSS - A Source Measurement Suite for Java" href="http://javancss.codehaus.org/" target="_blank">JavaNCSS</a> is a great place to start, but there are many more tools.
  * Tools to analyze the results. Adventurous types might feel like using an XSLT to process the XML that JavaNCSS can generate. I went with some very basic Python hacking and Excel.

## Analyzing the Sources

I used a small Windows command line script to check out revisions ranging from 20000 to 35000 in increments of 150, which gave me 101 measurements. The script looks like this:

<pre lang="winbatch">for /l %%r in (20000, 150, 35000) do (
  echo %%r
  svn co http://subversion/project/src/main/java@%%r project%%r
  c:\Java\Tools\javancss-32.53\bin\javancss -function -recursive c:\cyclomatic_compl\project%%r &gt; ncss%%r.txt
  rmdir project%%r /s /q
)
</pre>

It loops over the revision numbers we want. It checks out the revision, calculates the CCN and removes the directory. This will create 101 ncss.txt files with the JavaNCSS function-level reports for each revision.

That&#8217;s all there is to it.

## Analyzing the Results

Next I wanted to get some of those numbers in Excel. It was about time I picked up Python again, so I used some of my rusty knowledge to come up with the following code:

<pre lang="python">import glob

def process(filename, fout):
  revision = filename[24:29]
  print(revision)
  fin = open(filename, encoding="utf8")
  lines = fin.readlines()
  fin.close()
  fout.write(revision + ";")
  for i in [-4, -3, -1]:
    line = lines[i]
    value = line[line.rindex(" ")+1:-1]
    value = value.replace(",","").replace(".",",")
    fout.write(value + ";")
  fout.write("\n")

print("processing")

fout= open("result.csv", "w", encoding="utf8")
path="C:\\cyclomatic_compl\\ncss*.txt"
for filename in glob.glob(path):
  process(filename, fout)
</pre>

It&#8217;s not very pretty, but it manages its task: It loops over all the reports, extracts the values I&#8217;m interested in and creates a comma separated file. It also replaces the decimal separator due to an import bug in Excel.

## Conclusion

With a little bit of glue code, it&#8217;s fairly easy to get a feeling of how your projects complexity evolves over time. What you do with those measurements is up to you.

(<a title="Untitled on Flickr" href="http://www.flickr.com/photos/avrg/2875985830/" target="_blank">image credit</a>)

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->