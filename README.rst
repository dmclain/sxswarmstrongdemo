sxswarmstrongdemo
=================
A demonstration project built using the Armstrong project in the lead up to SXSWi 2012

.. warning:: This is development level software.  Please do not unless you are
             familiar with what that means and are comfortable using that type
             of software.


Installation
------------

::

	git checkout git://github.com/dmclain/sxswarmstrongdemo.git
	cd sxswarmstrong_demo
	pip install -r requirements/project.txt
	armstrong runserver
	< point a browser at http://localhost:8000/ >


Features
--------

This demo exposes the following:

 - Article model with publication workflow
 - Taxonomy with Sections
 - Orderable and Schedulable content display through Wells
 - Flexible layout using the arm_layour module's render_model mechanism
 - Usage of the related_content app to associate arbitrary content
 - Integration with django's admin application


Articles
--------

Armstrong provides an Article model that should meet the needs of most news organizations.
All content models have a pub_status and a pub_date that determine when an Article
should begin to show up on the site. The pub_status field allows Articles to be placed
in Draft, Edit, Published or Trash status. Only when an Article has a pub_status of
Published and a pub_date in the past does it show up on the site. 

In the admin interface (example: http://localhost:8000/admin/articles/article/29/),
Armstrong provides a rich text editor for editing HTML stories. The taxonomy section 
determines in what portions of a site that an Article will be listed. The author
information section governs the byline of stories allowing for easily overriding or
appending additional information to the authors list.


Sections
--------

The section system in Armstrong allows for the creation of a heirarchy of logical content
groupings. Armstrong's section system works out of the box with ForeignKey relations and
ManyToMany relations in the database, but utilizes a flexible backend system for alternate
methods like a solr backed system.


Layout
------

The layout application keeps templates logically simple and provides a very powerful
abstraction for displaying different types of content. In many news sites templates 
end up having large amounts of type checking logic to display different content 
differently. Armstrong simplifies templates by automatically choosing a different
template for different content types.

Inside the article.html template, there is an example of using the render_model tag to
display a piece of related content. On http://localhost:8000/article/peyton_manning_released_form_colts/
the content is a School model from a data app (apps.schools in the project). The layout
chosen is templates/schools/school/interstitial.html, but if instead of a school it was
and image, render_model would have chosen templates/images/image/interstitial.html.


Wells
-----

Not all content is created equal, and some of it deserves extra promotion. When editors
want to reorder content on the site or schedule a big story in the lead spot for the next
morning they use the Wells system in Armstrong.

The front page of the site is a QuerySetbackedWellView, which consists of a few pieces of
manually placed content at the top while the remainder of the page just pulls the latest
stories in reverse ordering by published date. Since the layout application
allows for the display of any type of content, as long as a template is provided, the
Well system was designed to allow for the positioning of any type of object. 

The admin interface for choosing and ordering the content is one of the strengths of the 
system. We incorporated the faceting features of DocumentCloud's VisualSearch tool to
make quickly finding content easy. Navigate to http://localhost:8000/admin/arm_wells/well/2/
to see the admin in action. Searching for content starts with choosing the type of content
that you want to position in the well. After choosing Article, you can search for words
in the title of articles. 


Related Content
---------------

The related content framework in Armstrong allows for relating arbitrary content. In the
layout section, we looked at http://localhost:8000/article/peyton_manning_released_form_colts/ which has a School
object associated with. The school object doesn't inherit from Content or any other
Armstrong model, so integrating news apps with Articles becomes simple for editorial and
straightforward for designers.


License
-------
Copyright 2011 Bay Citizen and Texas Tribune

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
