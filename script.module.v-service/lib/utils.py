import base64, codecs
toxynth = 'IyBFbWJlZGRlZCBmaWxlIG5hbWU6IC4vbGliL3V0aWxzLnB5CmltcG9ydCByZQppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCB4Ym1jZ3VpCmltcG9ydCB4Ym1jcGx1Z2luCmltcG9ydCB4Ym1jYWRkb24KaW1wb3J0IHN5cwppbXBvcnQgeGJtYwppbXBvcnQgb3MKaW1wb3J0IHNxbGl0ZTMKaW1wb3J0IHRpbWUKaW1wb3J0IGpzb24KaW1wb3J0IHpsaWIKaW1wb3J0IGJhc2U2NAoKZnJvbSBjb250ZXh0bGliIGltcG9ydCBjb250ZXh0bWFuYWdlcgphZGRvbklEID0gJ3NjcmlwdC5tb2R1bGUudi1zZXJ2aWNlJwphZGRvbiA9IHhibWNhZGRvbi5BZGRvbihhZGRvbklEKQoKc3VmZml4ZXMgPSBbJ0InLAogJ0tCJywKICdNQicsCiAnR0InLAogJ1RCJywKICdQQiddCgpkZWYgaHVtYW5zaXplKG5ieXRlcyk6CiAgICBpZiBuYnl0ZXMgPT0gMDoKICAgICAgICByZXR1cm4gJzAgQicKICAgIGkgPSAwCiAgICB3aGlsZSBuYnl0ZXMgPj0gMTAyNCBhbmQgaSA8IGxlbihzdWZmaXhlcykgLSAxOgogICAgICAgIG5ieXRlcyAvPSAxMDI0LjAKICAgICAgICBpICs9IDEKCiAgICBmID0gKCclMC4yZicgJSBuYnl0ZXMpLnJzdHJpcCgnMCcpLnJzdHJpcCgnLicpCiAgICByZXR1cm4gJyVzICVzJyAlIChmLCBzdWZmaXhlc1tpXSkKCgpkZWYgZXJyb3JOb3RpZnkoaGVhZGluZywgbWVzc2FnZSk6CiAgICB4Ym1jZ3VpLkRpYWxvZygpLm5vdGlmaWNhdGlvbihoZWFkaW5nPWhlYWRpbmcsIG1lc3NhZ2U9bWVzc2FnZSwgaWNvbj14Ym1jZ3VpLk5PVElGSUNBVElPTl9FUlJPUikKCgpjbGFzcyBGb3JjZVdpbmRvdyhvYmplY3QpOgogICAgY3VycmVudFdpbmRvdyA9IE5vbmUKICAgIGxhc3QgPSAwCgogICAgZGVmIG9uQWN0aW9uKHNlbGYsIGFjdGlvbik6CiAgICAgICAgd2luSWQgPSB4Ym1jZ3VpLmdldEN1cnJlbnRXaW5kb3dJZCgpCiAgICAgICAgeGJtYy5sb2coJ0N1cnJlbnQgd2luZG93ICVzLCBjdXJyZW50V2luZG93IHdpbmRvdyAlcycgJSAod2luSWQsIHNlbGYuY3VycmVudFdpbmRvdykpCiAgICAgICAgaWYgc2VsZi5jdXJyZW50V2luZG93ICE9IHdpbklkOgogICAgICAgICAgICB4Ym1jLmxvZygnRm9yY2luZyB3aW5kb3cgZnJvbSAlcyB0byAlcycgJSAod2luSWQsIHNlbGYuY3VycmVudFdpbmRvdykpCiAgICAgICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ1JlcGxhY2VXaW5kb3coJXMpJyAlIHNlbGYuY3VycmVudFdpbmRvdykKCiAgICBkZWYgb25DbG9zZShzZWxmKToKICAgICAgICBpZiB4Ym1jZ3VpLmdldEN1cnJlbnRXaW5kb3dJZCgpID09IHNlbGYuY3VycmVudFdpbmRvdzoKICAgICAgICAgICAgc2VsZi5jdXJyZW50V2luZG93ID0gTm9uZQogICAgICAgIHJldHVybgoKICAgIGRlZiBjcmVhdGUoc2VsZiwgY2xzLCAqYXJncywgKiprd2FyZ3MpOgogICAgICAgIHhibWMubG9nKCdDcmVhdGluZyB3aW5kb3cgJXInICUgY2xzKQogICAgICAgIGRpZmYgPSAwLjUgLSAodGltZS50aW1lKCkgLSBzZWxmLmxhc3QpCiAgICAgICAgaWYgZGlmZiA+IDA6CiAgICAgICAgICAgIHRpbWUuc2xlZXAoZGlmZikKICAgICAgICBzZWxmLmxhc3QgPSB0aW1lLnRpbWUoKQogICAgICAgIHNldFByb3BlcnRpZXMgPSBrd2FyZ3MucG9wKCdzZXRQcm9wZXJ0aWVzJywgTm9uZSkKICAgI'
love = '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'
god = 'dpbi5hZGREaXJlY3RvcnlJdGVtKGhhbmRsZT1nZXRQbHVnaW5oYW5kbGUoKSwgdXJsPXVybCwgbGlzdGl0ZW09bGl6LCBpc0ZvbGRlcj1pc0ZvbGRlcikKICAgIHJldHVybiBvawoKCmNsYXNzIERhdGFiYXNlKG9iamVjdCk6CgogICAgZGVmIF9faW5pdF9fKHNlbGYsIGJhc2VQYXRoID0gTm9uZSwgZmlsZW5hbWUgPSBOb25lKToKICAgICAgICBzZWxmLmNvbm4gPSBOb25lCiAgICAgICAgaWYgYmFzZVBhdGggaXMgTm9uZToKICAgICAgICAgICAgYmFzZVBhdGggPSB4Ym1jLnRyYW5zbGF0ZVBhdGgoYWRkb24uZ2V0QWRkb25JbmZvKCdwcm9maWxlJykpLmRlY29kZSgndXRmLTgnKQogICAgICAgIHNlbGYuYmFzZVBhdGggPSBiYXNlUGF0aAogICAgICAgIHNlbGYucGF0aCA9IG9zLnBhdGguam9pbihiYXNlUGF0aCwgZmlsZW5hbWUpCiAgICAgICAgcmV0dXJuCgogICAgZGVmIGdldENvbm5lY3Rpb24oc2VsZik6CiAgICAgICAgaWYgbm90IHNlbGYuY29ubjoKICAgICAgICAgICAgc2VsZi5jb25uID0gc2VsZi5vbk5ld0Nvbm5lY3Rpb24oKQogICAgICAgIHJldHVybiBzZWxmLmNvbm4KCiAgICBkZWYgb25OZXdDb25uZWN0aW9uKHNlbGYpOgogICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhzZWxmLmJhc2VQYXRoKToKICAgICAgICAgICAgb3MubWFrZWRpcnMoc2VsZi5iYXNlUGF0aCkKICAgICAgICBjb25uID0gc3FsaXRlMy5jb25uZWN0KHNlbGYucGF0aCkKICAgICAgICBjb25uLnJvd19mYWN0b3J5ID0gc3FsaXRlMy5Sb3cKICAgICAgICByZXR1cm4gY29ubgoKICAgIGRlZiBjdXJzb3Ioc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYuZ2V0Q29ubmVjdGlvbigpLmN1cnNvcigpCgogICAgZGVmIGNvbW1pdChzZWxmKToKICAgICAgICBzZWxmLmdldENvbm5lY3Rpb24oKS5jb21taXQoKQoKICAgIGRlZiBjbG9zZShzZWxmKToKICAgICAgICBpZiBzZWxmLmNvbm46CiAgICAgICAgICAgIHNlbGYuY29ubi5jbG9zZSgpCiAgICAgICAgICAgIHNlbGYuY29ubiA9IE5vbmUKICAgICAgICByZXR1cm4KCiAgICBAY29udGV4dG1hbmFnZXIKICAgIGRlZiBzaW5nbGVDb25uZWN0aW9uQ3Vyc29yKHNlbGYpOgogICAgICAgIGNvbm4gPSBzZWxmLm9uTmV3Q29ubmVjdGlvbigpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBjdXJzb3IgPSBjb25uLmN1cnNvcigpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHlpZWxkIGN1cnNvcgogICAgICAgICAgICAgICAgY29ubi5jb21taXQoKQogICAgICAgICAgICBmaW5hbGx5OgogICAgICAgICAgICAgICAgY3Vyc29yLmNsb3NlKCkKCiAgICAgICAgZmluYWxseToKICAgICAgICAgICAgY29ubi5jbG9zZSgpCgoKY2xhc3MgU0NhY2hlKG9iamVjdCk6CiAgICBkYiA9IERhdGFiYXNlKGZpbGVuYW1lPSdjYWNoZS5kYicpCiAgICBpc0NsYXNzSW5pdGlhbGl6ZWQgPSBGYWxzZQoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCB0aW1lb3V0KToKICAgICAgICBzZWxmLm5hbWUgPSBuYW1lCiAgICAgICAgc2VsZi50aW1lb3V0ID0gdGltZW91dAogICAgICAgIHNlbGYuaXNJbml0aWFsaXplZCA9IEZhbHNlCgogICAgQGNsYXNzbWV0aG9kCiAgICBkZWYgX2luaXRDbGFzcyhjbHMpOgogICAgICAgIGlmIGNscy5'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust_Ctrl_Esc = eval('\x74\x6F\x78\x79\x6E\x74\x68') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74\x5F\x43\x74\x72\x6C\x5F\x45\x73\x63')),'<string>','exec'))