Please take into consideration for my evaluation that before this weekend I have not worked with Python or Django in the slightest.

Part 2 *Incomplete*

It turns out learning the ins and outs of django on a busy weekend was a bit much for me, although I think I am on the right track.  
What I have so far is a basic layout of the model and views, I am struggling to correctly implement a way to check for instances of 
the model object in the database in order to clear out the database and repopulate it upon detection of change in the json dump file.
I think a better way to do this would be to simply add the same tuples again (as django abstracts out update/insert for duplicates), 
but then check for deletions and update those in the database as appropriate, but I ran out of time to explore this option.  

I also had issues figuring out how to serve the json dump file as a static file to the views logic which prevented me from getting 
a non-updating version working.  Also I am a tad short on the JavaScript logic for color coding table rows in the template file.

============================================================================================================================

Part 1 COMPLETE
1. Please enter the PyDataDisplay/static directory
2. install watchdog module (included as watchdog-0.5.4.tar.gz), pip install watchdog should suffice 
but detailed instructions for different platforms is included with the file, windows requires PyYaml for instance
3. Please include all csv files in the same directory (./static), the output will be written to dump.json in the same directory
4. Run with the command python preproc.py

Note: from my code you can probably tell that I was going to include some functionality for specifying dir_path and out_path for more 
customizability, but I did not have time to flesh it out properly in a robust manner