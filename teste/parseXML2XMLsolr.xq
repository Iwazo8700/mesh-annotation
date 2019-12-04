let $mesh := doc("/home/enzo/Documentos/Docker/desc2020.xml")

return
<add>
{
  for $d in ($mesh//DescriptorRecord)
  return
  <doc>
     <field name="DescriptorUI">{$d/DescriptorUI/text()}</field>
     <field name="DescriptorName">{$d/DescriptorName/String/text()}</field>
     <field name="DateCreated">{$d/DateCreated/Year/text()}-{$d/DateCreated/Month/text()}-{$d/DateCreated/Day/text()}</field>
     {
       for $c in ($d//ConceptUI)
       return
       <field name="ConceptUI">{$c/text()}</field>
     }
     <field name="Annotation">{$d//Annotation/text()}</field>
     <field name="ScopeNote">{$d//ScopeNote/text()}</field>
     {
       for $pa in ($d//PharmacologicalAction) 
         return 
         <field name="PharmacologicalAction">{$pa/DescriptorName/String/text()}</field>
     }
     
     
  </doc>
}
</add>