# revolt.py Superembeds
Superembeds is an extension of revolt.py's embeds which aims to make using embeds a lot easier (especially for those
who've used embeds in discord.py and similar before).

Features:
- Makeshift embed fields
  - Please do note that **this does not use any actual embed fields**. As Revolt doesn't support having fields in embeds
yet, we had to resort to showing the field data in the embed description, rather than in actual fields like we can
on Discord and Guilded.
- Ability to use integers to set color

## Examples
To send an embed with a field in revolt.py:
```py
import revolt
import embed as revoltembed

...

embed = revoltembed.Embed(title='Hello world!', description='This is an embed!')
embed.add_field(name='This is an embed field!', value='(well, not exactly)')
await ctx.send(embed=embed)
```

Or to remove a field from an embed:
```py
embed = revoltembed.Embed(title='Hello world!', description='This is an embed!')
embed.add_field(name='This is an embed field!', value='(well, not exactly)')
embed.remove_field(0)
```

Or to insert a field:
```py
embed = revoltembed.Embed(title='Hello world!', description='This is an embed!')
embed.add_field(name='This is an embed field!', value='(well, not exactly)')
embed.add_field(name='This is another embed field!', value='Embed fields are shown using the embed description.')
embed.insert_field_at(1, name='This is an inserted field!', value='enjoy :)')
```

## Limitations
- Like we've said before, **this does NOT use actual "fields"**. All embed fields will be added to the embed
  description for display.
- Due to this, inline fields are not possible.
