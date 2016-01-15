<?php
	header('Content-type: application/xml');
	$PUBMEDID = $_GET['PubMedID'] ;
	$link = mysql_connect('localhost', 'root','powers1');
	mysql_select_db( 'project3_db', $link ) ;
	$sql = "SELECT Authors.Authors,Citations.Title,Citations.journal,Citations.volume, Citations.pages, Citations.year from Reference LEFT JOIN Citations on (Reference.PubMedID = Citations.PubMedID) Left Join Authors on (Reference.PubMedId = Authors.PubMedId) WHERE Reference.PubMedID ='".$PUBMEDID."'" ;
	$result = mysql_query($sql) ;
?>
<response>
<?php
		while($row = mysql_fetch_assoc($result))
        	{

	 		
			$Author = $row['Authors'];
			$Title = $row['Title'];
			$journal = $row['journal'];
			$Volume = $row['volume'];
			$pages = $row['pages'];
			$year = $row['year'];
			
			
?>		
	    
	
		
		<author><?php echo $Author ?></author>
		<Title><?php echo $Title ?></Title>
		<journal><?php echo $journal ?></journal>
		<Volume><?php echo $Volume ?></Volume>
		<pages><?php echo $pages ?></pages>
		<year><?php echo $year ?></year>
<?php
         }
         
?>         		
</response>
