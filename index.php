<?php
// Falls es ohne Parameter aufgerufen wird, einfach abbrechen
if (!isset($_GET["tag"]))
{
	$error = true;
}
else
{
	$error = false;
	// Aktuelles Datum, Tag, Monat
	date_default_timezone_set("Europe/Berlin");
	$timestamp = time();
	$intTag = date ('j', $timestamp);
	$intMonat = date ('m', $timestamp);

	// Das alles nur im Dezember ausführen:
	if ($intMonat == 12) 
	{
		$strTag = $_GET["tag"];

		// Alle Parameter abholen, json auslesen, verarbeiten usw.
		$file = 'songs.json';
		$filecontent = file_get_contents($file);
		$songlist = json_decode($filecontent, true);

		
		foreach($songlist as $song)
		{
			if ($song['Guid'] == $strTag)
			{
				if ($intTag < intval($song['Day']))
				{
					$error = true;
				}
			}
		}
	}
	else
	{ 
		$error = true;
	}
}

if ($error == true)
{
	echo "Hast du geschummelt?";
}
else
{
	header('Location: ' . $song['Link']);
	exit;
}
?>
