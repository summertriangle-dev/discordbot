import loader

@loader.command("help",
    description="Display commands' help messages.")
async def help(context, message, content):
    inspect_cmd = loader.ROOT_COMMAND

    for word in content.split():
        if word in inspect_cmd.sub_dispatch_table:
            inspect_cmd = inspect_cmd.sub_dispatch_table[word]

        for cmd_struct in inspect_cmd.sub_dispatch_table.values():
            if word in cmd_struct.extwords:
                inspect_cmd = cmd_struct
                break

    context.arg0 = content
    await loader.Command.default_implementation(inspect_cmd,
        context, message, content)
