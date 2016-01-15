<?php

	header('Content-type: application/xml');
	$link = mysql_connect('localhost', 'root', 'powers1');
	mysql_select_db( 'project3_db', $link ) ;
	$sql = "SELECT uniproid FROM E2_sequence" ;
	$result = mysql_query($sql) ;
?>
<response>
<?php
		while($row = mysql_fetch_assoc($result))
        	{

        		$uniprotID = $row['uniproid'] ;
?>
				<uniprotid><?php echo $uniprotID ?></uniprotid>
<?php
}
?>
</response>
