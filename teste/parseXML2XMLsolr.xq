let $mesh := doc("/home/enzo/Documentos/Docker/mesh-annotation/teste/desc2020.xml")

return
<add>
{
  for $d in ($mesh//DescriptorRecord)
  return
  <doc>
     <field name="id">{$d/DescriptorUI/text()}</field>
     <field name="descriptor_name">{$d/DescriptorName/String/text()}</field>
     <field name="date_created">{$d/DateCreated/Year/text()}-{$d/DateCreated/Month/text()}-{$d/DateCreated/Day/text()}</field>
     {
       for $c in ($d//ConceptUI)
       return
       <field name="conceptUI">{$c/text()}</field>
     }
  </doc>
}
</add>