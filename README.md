# Revolt.py Superembeds
Superembeds is an extension of Revolt.py's embeds which aims to make using embeds a lot easier (especially for those
who've used embeds in discord.py and similar before).

Features:
- Makeshift embed fields and footers
  - Please do note that **this does not use any actual embed fields or footers**. As Revolt doesn't support having
    fields and footers in embeds yet, we had to resort to showing them through the embed description, rather than in
    actual fields like we can on Discord and Guilded.
- Ability to use hex integers (e.g. `0xffb5ee`) to set color

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

You can also set a footer text:
```py
embed = revoltembed.Embed(title='Hello world!', description='This is an embed!')
embed.set_footer(text='Made by UnifierHQ')
```

## Limitations
- Like we've said before, **this does NOT use actual "fields" or "footers"**. All embed fields and footers will be
  added to the embed description to be displayed.
- Due to this, inline fields are not possible.
- Footers only support text, as there's no way to add inline attachments on Revolt.
