from tkinter import Tk, font
root = Tk()
print(font.families())

'''('System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif',
'Small Fonts', '8514oem', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 
'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold',
'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 
'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 
'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light',
'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium',
'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console',
'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 
'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', 
'@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa',
'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 
'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti',
'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'MingLiU_MSCS-ExtB', 
'@MingLiU_MSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic',
'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Nirmala Text', 'Nirmala Text Semilight', 'Palatino Linotype',
'Sans Serif Collection', 'Segoe Fluent Icons', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black',
'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 
'Segoe UI Variable Small Light', 'Segoe UI Variable Small Semilig', 'Segoe UI Variable Small', 'Segoe UI Variable Small Semibol',
'Segoe UI Variable Text Light', 'Segoe UI Variable Text Semiligh', 'Segoe UI Variable Text', 'Segoe UI Variable Text Semibold',
'Segoe UI Variable Display Light', 'Segoe UI Variable Display Semil', 'Segoe UI Variable Display', 'Segoe UI Variable Display Semib',
'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Small Semibold', 'Sitka Text', 
'Sitka Text Semibold', 'Sitka Subheading', 'Sitka Subheading Semibold', 'Sitka Heading', 'Sitka Heading Semibold', 'Sitka Display',
'Sitka Display Semibold', 'Sitka Banner', 'Sitka Banner Semibold', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 
'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings'
, 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', 
'@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', 
'@Yu Gothic UI Semilight', 'SimSun-ExtG', '@SimSun-ExtG', 'Agency FB', 'Algerian', 'Book Antiqua', 'Arial Narrow', 'Arial Rounded MT Bold',
'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Bernard MT Condensed', 'Bodoni MT', 'Bodoni MT Black', 'Bodoni MT Condensed',
'Bodoni MT Poster Compressed', 'Bookman Old Style', 'Bradley Hand ITC', 'Britannic Bold', 'Berlin Sans FB', 'Berlin Sans FB Demi', 
'Broadway', 'Brush Script MT', 'Bookshelf Symbol 7', 'Californian FB', 'Calisto MT', 'Castellar', 'Century Schoolbook', 'Centaur', 
'Century', 'Chiller', 'Colonna MT', 'Cooper Black', 'Copperplate Gothic Bold', 'Copperplate Gothic Light', 'Curlz MT', 'Dubai', 
'Dubai Light', 'Dubai Medium', 'Elephant', 'Engravers MT', 'Eras Bold ITC', 'Eras Demi ITC', 'Eras Light ITC', 'Eras Medium ITC',
'Felix Titling', 'Forte', 'Franklin Gothic Book', 'Franklin Gothic Demi', 'Franklin Gothic Demi Cond', 'Franklin Gothic Heavy', 
'Franklin Gothic Medium Cond', 'Freestyle Script', 'French Script MT', 'Footlight MT Light', 'Garamond', 'Gigi', 'Gill Sans MT',
'Gill Sans MT Condensed', 'Gill Sans Ultra Bold Condensed', 'Gill Sans Ultra Bold', 'Gloucester MT Extra Condensed', 'Gill Sans MT Ext Condensed Bold',
'Century Gothic', 'Goudy Old Style', 'Goudy Stout', 'Harlow Solid Italic', 'Harrington', 'Haettenschweiler', 'High Tower Text', 
'Imprint MT Shadow', 'Informal Roman', 'Blackadder ITC', 'Edwardian Script ITC', 'Kristen ITC', 'Jokerman', 'Juice ITC', 
'Kunstler Script', 'Wide Latin', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Lucida Handwriting', 'Lucida Sans',
'Lucida Sans Typewriter', 'Magneto', 'Maiandra GD', 'Matura MT Script Capitals', 'Mistral', 'Modern No. 20', 'Monotype Corsiva', 
'MT Extra', 'Niagara Engraved', 'Niagara Solid', 'OCR A Extended', 'Old English Text MT', 'Onyx', 'MS Outlook', 'Palace Script MT',
'Papyrus', 'Parchment', 'Perpetua', 'Perpetua Titling MT', 'Playbill', 'Poor Richard', 'Pristina', 'Rage Italic', 'Ravie', 
'MS Reference Sans Serif', 'MS Reference Specialty', 'Rockwell Condensed', 'Rockwell', 'Rockwell Extra Bold', 'Script MT Bold', 
'Showcard Gothic', 'Snap ITC', 'Stencil', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Tw Cen MT Condensed Extra Bold', 'Tempus Sans ITC', 
'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wingdings 2', 'Wingdings 3', 'Cascadia Code ExtraLight', 'Cascadia Code Light',
'Cascadia Code SemiLight', 'Cascadia Code', 'Cascadia Code SemiBold', 'Cascadia Mono ExtraLight', 'Cascadia Mono Light', 
'Cascadia Mono SemiLight', 'Cascadia Mono', 'Cascadia Mono SemiBold')'''
