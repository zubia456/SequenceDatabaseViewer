<?php
	header('Content-type: application/xml');
	$uniprotID = $_GET['uniproid'] ;
	$link = mysql_connect('localhost', 'root','powers1');
	mysql_select_db( 'mysql_db', $link ) ;
	$sql = "SELECT Reference.PubMedID, E2_sequence.fullname, E2_sequence.organism, E2_sequence.sequence from Reference LEFT JOIN Citations on (Reference.PubMedID = Citations.PubMedID) LEFT JOIN E2_sequence on (Reference.uniproid = E2_sequence.uniproid) where Reference.uniproid = '".$uniprotID."'";
	$result = mysql_query($sql) ;
?>
<response>
<?php
	while($row = mysql_fetch_assoc($result))
	{
	  $PubMed = $row['PubMedID'];
	  $fullname = $row['fullname'];
	  $organism = $row['organism'];
	  $sequence = $row['sequence'];

		
?>		
	    
	  <PubMed><?php echo $PubMed ?></PubMed>
	  <fullname><?php echo $fullname ?></fullname>
	  <organism><?php echo $organism ?></organism>
	  <sequence><?php echo $sequence ?></sequence>
<?php
	}
?>		
		
</response>
