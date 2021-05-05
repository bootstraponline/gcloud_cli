)
def write_commit_patch(f, commit, contents, progress, version=None, encoding=None):
    Args:
      commit: Commit object
      progress: Tuple with current patch number and total.
    Returns:
      tuple with filename and contents
    f.write(
        b"From "
        + commit.id
        + b" "
        + time.ctime(commit.commit_time).encode(encoding)
        + b"\n"
    )
    f.write(
        b"Date: " + time.strftime("%a, %d %b %Y %H:%M:%S %Z").encode(encoding) + b"\n"
    )
    f.write(
        ("Subject: [PATCH %d/%d] " % (num, total)).encode(encoding)
        + commit.message
        + b"\n"
    )

        p = subprocess.Popen(
            ["diffstat"], stdout=subprocess.PIPE, stdin=subprocess.PIPE
        )

    Args:
      commit: Commit
    Returns: Summary string
    decoded = commit.message.decode(errors="replace")
    return decoded.splitlines()[0].replace(" ", "-")
        return "{}".format(beginning)
    return "{},{}".format(beginning, length)


def unified_diff(
    a,
    b,
    fromfile="",
    tofile="",
    fromfiledate="",
    tofiledate="",
    n=3,
    lineterm="\n",
    tree_encoding="utf-8",
    output_encoding="utf-8",
):
            fromdate = "\t{}".format(fromfiledate) if fromfiledate else ""
            todate = "\t{}".format(tofiledate) if tofiledate else ""
            yield "--- {}{}{}".format(
                fromfile.decode(tree_encoding), fromdate, lineterm
            ).encode(output_encoding)
            yield "+++ {}{}{}".format(
                tofile.decode(tree_encoding), todate, lineterm
            ).encode(output_encoding)
        yield "@@ -{} +{} @@{}".format(file1_range, file2_range, lineterm).encode(
            output_encoding
        )
            if tag == "equal":
                    yield b" " + line
            if tag in ("replace", "delete"):
                    if not line[-1:] == b"\n":
                        line += b"\n\\ No newline at end of file\n"
                    yield b"-" + line
            if tag in ("replace", "insert"):
                    if not line[-1:] == b"\n":
                        line += b"\n\\ No newline at end of file\n"
                    yield b"+" + line
    Args:
      content: Bytestring to check for binary content
    return b"\0" in content[:FIRST_FEW_BYTES]
    Args:
      f: File-like object to write to
      store: Store to retrieve objects from, if necessary
      old_file: (path, mode, hexsha) tuple
      new_file: (path, mode, hexsha) tuple
      diff_binary: Whether to diff files even if they
    Note: the tuple elements should be None for nonexistant files
    patched_old_path = patch_filename(old_path, b"a")
    patched_new_path = patch_filename(new_path, b"b")
            return Blob.from_string(b"")
            return Blob.from_string(b"Subproject commit " + hexsha + b"\n")

    f.writelines(
        gen_diff_header((old_path, new_path), (old_mode, new_mode), (old_id, new_id))
    )
    if not diff_binary and (is_binary(old_content.data) or is_binary(new_content.data)):
        binary_diff = (
            b"Binary files "
            + patched_old_path
            + b" and "
            + patched_new_path
            + b" differ\n"
        )
        f.write(binary_diff)
        f.writelines(
            unified_diff(
                lines(old_content),
                lines(new_content),
                patched_old_path,
                patched_new_path,
            )
        )
    Args:
      paths: Tuple with old and new path
      modes: Tuple with old and new modes
      shas: Tuple with old and new shas
    if old_path is None and new_path is not None:
        old_path = new_path
    if new_path is None and old_path is not None:
        new_path = old_path
    old_path = patch_filename(old_path, b"a")
    new_path = patch_filename(new_path, b"b")

                yield ("old file mode %o\n" % old_mode).encode("ascii")
            yield ("new file mode %o\n" % new_mode).encode("ascii")
            yield ("deleted file mode %o\n" % old_mode).encode("ascii")
    if new_mode is not None and old_mode is not None:
        yield (" %o" % new_mode).encode("ascii")
    Args:
      f: File-like object to write to
      old_file: (path, mode, hexsha) tuple (None if nonexisting)
      new_file: (path, mode, hexsha) tuple (None if nonexisting)
    Note: The use of write_object_diff is recommended over this function.
    patched_old_path = patch_filename(old_path, b"a")
    patched_new_path = patch_filename(new_path, b"b")

    f.writelines(
        gen_diff_header(
            (old_path, new_path),
            (old_mode, new_mode),
            (getattr(old_blob, "id", None), getattr(new_blob, "id", None)),
        )
    )
    f.writelines(
        unified_diff(old_contents, new_contents, patched_old_path, patched_new_path)
    )
    Args:
      f: File-like object to write to.
      old_tree: Old tree id
      new_tree: New tree id
      diff_binary: Whether to diff files even if they
        write_object_diff(
            f,
            store,
            (oldpath, oldmode, oldsha),
            (newpath, newmode, newsha),
            diff_binary=diff_binary,
        )
    Args:
      f: File-like object to parse
      encoding: Encoding to use when creating Git objects
    Returns: Tuple with commit object, diff contents and git version
    if isinstance(contents, bytes) and getattr(email.parser, "BytesParser", None):
    Args:
      msg: An email message (email.message.Message)
      encoding: Encoding to use to encode Git commits
    Returns: Tuple with commit object, diff contents and git version
        subject = msg["subject"][close + 2 :]
                c.author = line[len(b"From: ") :].rstrip()