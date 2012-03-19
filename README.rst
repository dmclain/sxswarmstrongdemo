armstrong.apps.articles
=======================
Provides a basic Article model for Armstrong

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

Articles
--------


Sections
--------


Wells
-----


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



Related Content
---------------


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
