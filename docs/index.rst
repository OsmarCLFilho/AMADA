.. AMADA documentation master file, created by
   sphinx-quickstart on Sun Oct  2 11:09:10 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AMADA's documentation!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

* :ref:`Data Sources`
* :ref:`Extraction Scripts`
* :ref:`Analysis Scripts`
* :ref:`Basis`

.. _Data Sources:

Data Sources
------------

The data sources used in the project are located under the *data* folder. They are comprised of csv and txt files and contain either actual data or links to site to be *web scraped*.

lyrics.csv
**********

`lyrics.csv`, obtained from https://www.kaggle.com/datasets/ggapp1/arctic-monkeys-lyrics, is a dataset with the names, repective album and lyrics of most Arctic Monkeys' tracks.

to_scrape.txt
*************

`to_scrape.txt` is a list of useful links from web_scraping data. However, in the end, only https://en.wikipedia.org/wiki/Arctic_Monkeys_discography was used.

tvappear.txt
************

`tvappear.txt` is a list of tv series and the Arctic Monkeys' tracks that are used in them.

.. _Extraction Scripts:

Extraction Scripts
------------------

The extraction scripts are located under the *scripts* folder. They are responsible for obtaining and organizing data into useful formats so that the analysis scripts can be executed over such data.

spot_datax.py
*************

`spot_datax.py` (spotify data extraction) is responsible for data about tracks through the Spotify API. Such task is done with the Spotipy library and yields the `spot_data.csv` file under *results*.

lyrics_enjoyer.py
*****************

`lyrics_enjoyer.py` (lyrics joiner) is responsible for adding the `lyrics.csv` data into the `spot_data.csv`, creating the `spo_lyr_data.csv` file.

wikipedist.py
*************

`wikipedist.py` is responsible for web_scraping https://en.wikipedia.org/wiki/Arctic_Monkeys_discography for the album certifications table. It then adds the collected information into `spo_lyr_data` to generate `final_dataset.csv`.

.. _Analysis Scripts:

Analysis Scripts
----------------

The analysis scripts are located under the *scripts* folder. They are responsible for analysing the refined data from the extraction scripts and producing useful information and statistics.

etap2_g1.py
***********

`etap2_g1.py` is responsible for answering the first group of questions. Running it will print the answers. It does so through the following functions:

.. function:: popularity(album)

   Prints the most and the least popular track in an album

   :param str album: The album in which to search the tracks
   :rtype: None


.. function:: durations(album)

   Prints the longest and the shortest track in an album

   :param str album: The album in which to search the tracks
   :rtype: None


.. function:: allpopularity()

   Prints the most and the least popular track in all the albums

   :rtype: None


.. function:: allduration()

   Prints the longest and the shortest track in all the albums

   :rtype: None

.. function:: awards()

   Prints the albums with the most golden and platinum certifications

   :rtype: None

.. function:: correlation()

   Prints the correlation between the duration and popularity

   :rtype: None

etap2_g2.py
***********

`etap2_g2.py` is responsible for answering the first group of questions. Running it will print the answers. It does it through functions contained in `func_etapa2_g2.py`.

func_etapa2_g2.py
^^^^^^^^^^^^^^^^^

.. function:: concat_elements_column(df, col, key=None)

   Concatenates all the strings in the *col* column and return it as a dictionary with a single key *"all"* and the concatenated strings; if *key* is None. Else, returns a dictionary with keys correponding to the values of the column *key*, each followed by its respective value from *col*. 

   :param pandas.DataFrame df: The dataframe that the function will operate over.
   :param str col: Column whose values will be concatenated or put into the returning dictionary.
   :param str key: Column whose values will act as keys for the returning dictionary. If None, then returns a single key dictionary with the concatenated values of *col*.

   :return: Either a single key dictionary with the concatenated values or an extensive dictionary with *key* elements as keys and *col* elements as values.


.. function:: remove_contractions(dictionary)

   Removes most common contractions from *dictionary*, i.e.: *'M*, *'S*, *'RE*, *N'T*, *'LL*, *'VE*, *'D*.

   :param dict dictionary: Dictionary filled with string values.

   :return: Dictionary without the contractions.


.. function:: remove_characters(dictionary)

   Removes special characters from *dictionary*, i.e.: *( ) ? ! [ ] , . / & \ ' - : ; "*

   :param dict dictionary: Dictionary filled with string values.

   :return: Dictionary without the special characters


.. function:: remove_undesirables(dictionary)

   Removes the undesirable words listed in *stopwords.txt*, such as articles, prepositions and the verb to be, from *dictionary*.

   :param dict dictionary: Dictionary filled with string values.

   :return: Dictionary of same size and keys, but with the original strings stripped of the undesirable words and turned into lists of words.


.. function:: elements_freq(dictionary)

   Counts how many times each word showed up in each of the lists of words of *dictionary*. It then return a dictionary of same size and keys, but with Panda series with the words as index and each corresponding word count as value.

   :param dict dictionary: Dictionary filled with lists of words.

   :return: Dictionary of same size and key, but filled with Panda series with the words as index and the respective word counts as values.


.. function:: relevancy(dictionary)

   Counts how many times each key of *dictionary* shows up in its corresponding value.

   :param dict dictionary: Dictionary filled with string values

   :return: Dictionary of same size and keys, but with the values replaced by the count of how many times the key showed up in the value.

tvappear.py
***********

`tvappear.py` is responsible for answering in what tv shows, series or other related media Arctic Monkeys' music is used in. It uses data from `tvappear.txt`.

.. function:: TV(song)

   Prints the TV shows in which *song* is used.

   :param str song: Name of the song to seach for.

   :rtype: None

.. function:: TVshows()

   Prints the shows that have at least one Arctic Monkeys music.

   :rtype: None

.. function:: songsInShow(show)

   Prints all the Arctic Monkeys tracks in the *show*.

   :param str show: Name of the show to search in

   :rtype: None

viz_g1.py
*********

`viz_g1.py` is responsible for generating graphical visualizations for the questions from the first group of questions. Output is placed into `viz_g1_out/`.

visualizacao_e2_g2.py
*********************

`visualizacao_e2_g2.py` is responsible for generating word clouds for questions 1, 2 and 4 of the second question group. Output is placed into `visualizacao_e2_g2_out.py/`.

.. _Results:

Results
-------

The results, located in the *results* folder, are datasets and csv created by the extraction scripts. These files contain the data over which the analysis scripts draw answers from.

spot_data.csv
*************

`spot_data.csv` is the file generated by `spot_datax.py`. It contains data pulled from the `Spotify API`, e.g.: popularity, duration, tempo, etc..

spo_lyr_data.csv
****************

`spo_lyr_data.csv` is the file fenerated by `lyrics_enjoyer.py`. It contains data from `spot_data.csv` plus data from `lyrics.csv`.

good_band_certs.csv
*******************

`good_band_certs.csv` is an file previously generated by `wikipedist.py`. It contains data about the albums certifications. It is now deprecated as its data is directly merged with `spo_lyr_data.csv` by `wikipedist.py` 

final_dataset.csv
*****************

`final_dataset.csv` is the merging of `spo_lyr_data.csv` with the certifications data from `wikipedist.py`. Other than the TV series tracks, it contains all the important data for the analysis scripts.
