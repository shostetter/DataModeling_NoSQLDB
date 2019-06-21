# **Sparkify: User Activity Data Modeling with Cassandra**  
## Background:
The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.
  
The *ETL_Pipeline_Cassandra.ipynb* Jupyter Notebook will create this database as well as run queries to answer the 3 questions provided by the analysis team. 

## Raw Datasets
There is one dataset: **event_data**. The directory of CSV files partitioned by date.   
Here are examples of filepaths to two files in the dataset:  
 * event_data/2018-11-08-events.csv  
 * event_data/2018-11-09-events.csv
 
## The results of the preprocessing step [*CassandraPreprocessing.py*] yields one CSV file titled <font color=red>event_datafile_new.csv</font>, located within the Workspace directory.  The event_datafile_new.csv contains the following columns: 
- artist 
- firstName of user
- gender of user
- item number in session
- last name of user
- length of the song
- level (paid or free song)
- location of the user
- sessionId
- song title
- userId

The image below is a screenshot of how the denormalized data should appear in the <font color=red>**event_datafile_new.csv**</font> after the preprocessing code above is run:<br>

<img src="images/image_event_datafile_new.jpg">


### 1. Question 1: <br>Select artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4:  <br
>Faithless | Music Matters (Mark Knight Dub) | 495.3073

### 1. Question 2: <br>Select artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4:  <br>
Down To The Bone | Keep On Keepin' On | Sylvie Cruz<br>
	 Three Drives | Greece 2000 | Sylvie Cruz<br>
	 Sebastien Tellier | Kilometer | Sylvie Cruz<br>
	 Lonnie Gordon | Catch You Baby (Steve Pitron & Max Sanna Radio Edit) | Sylvie Cruz</font>  
     
### 1. Question 3: <br>Select every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own':  <br>
Jacqueline Lynch<br>
	 Tegan Levine<br>
	 Sara Johnson 
