import base64, codecs
toxynth = 'ICAgICMgdW5jb21weWxlNiB2ZXJzaW9uIDMuNi40CiMgUHl0aG9uIGJ5dGVjb2RlIDIuNyAoNjIyMTEpCiMgRGVjb21waWxlZCBmcm9tOiBQeXRob24gMi43LjE3IChkZWZhdWx0LCBTZXAgMzAgMjAyMCwgMTM6Mzg6MDQpIAojIFtHQ0MgNy41LjBdCiMgRW1iZWRkZWQgZmlsZSBuYW1lOiAuL2xpYi9saXN0cy5weQojIENvbXBpbGVkIGF0OiAyMDE5LTAzLTExIDA1OjAyOjE5CmltcG9ydCB1dGlscywgeGJtYywgdXJsbGliMiwgb3MsIGJhc2U2NApBQ1RJT05TID0geydraWRzJzogJ0tpbmRlcicsIAogICAnZXJvdGljJzogJ0Vyb3RpaycsIAogICAnbWVkaWF0aGVrJzogJ01lZGlhdGhla2VuJ30KCmRlZiBraWRzKHBhcmFtcyk6CiAgICBpY29uQmFzZSA9ICdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIHV0aWxzLmFkZG9uSUQgKyAnL3Jlc291cmNlcy9raWRzLycKICAgIHV0aWxzLmFkZERpcignS2luZGVyZmlsbWUnLCAncGx1Z2luOi8vc2NyaXB0Lm1vZHVsZS52LXNlcnZpY2UvP2FjdGlvbj1pbmRleE1vdmllJmdlbnJlPUZhbWlsaWUsS2luZGVyLEp1Z2VuZCxUcmlja2ZpbG0mdHlwZT1tb3ZpZScsICdEZWZhdWx0TW92aWVzLnBuZycpCiAgICB1dGlscy5hZGREaXIoJ0tpbmRlcnNlcmllbicsICdwbHVnaW46Ly9zY3JpcHQubW9kdWxlLnYtc2VydmljZS8/YWN0aW9uPWluZGV4U2VyaWUmZ2VucmU9RmFtaWxpZSxLaW5kZXIsS2luZGVyc2VyaWUsSnVnZW5kLFRyaWNrZmlsbSZ0eXBlPXNlcmllJywgJ0RlZmF1bHRUVlNob3dzLnBuZycpCiAgICB1dGlscy5hZGREaXIoJ05pY2tlbG9kZW9uJywgJ3BsdWdpbjovL3BsdWdpbi52aWRlby5uaWNrX2RlLz9tb2RlPWxpc3RTaG93cyZwYWdlPTEmdXJsPWh0dHAlM2ElMmYlMmZ3d3cubmljay5kZSUyZnZpZGVvcycsIHhibWMudHJhbnNsYXRlUGF0aChpY29uQmFzZSArICdpY29uTmljay5wbmcnKSkKICAgIHV0aWxzLmFkZERpcignTmljayBKdW5pb3InLCAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLm5pY2tfZGUvP21vZGU9bmlja0pyTWFpbicsIHhibWMudHJhbnNsYXRlUGF0aChpY29uQmFzZSArICdpY29uTmljay5wbmcnKSkKICAgIHV0aWxzLmFkZERpcignS0lLQSsnLCAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmtpa2FfZGUnLCB4Ym1jLnRyYW5zbGF0ZVBhdGgoaWNvbkJhc2UgKyAnaWNvbktJS0EucG5nJykpCiAgICB1dGlscy5hZGREaXIoJ1Nlc2Ftc3RyYVx4YzNceDlmZScsICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uc2VzYW1zdHJhc3NlX2RlJywgeGJtYy50cmFuc2xhdGVQYXRoKGljb25CYXNlICsgJ2ljb25TUy5wbmcnKSkKCgpkZWYgZXJvdGljKHBhcmFtcyk6CgogICAgZGVmIHVybChwbHVnaW4sIHUpOgogICAgICAgIGZpZWxkcyA9ICgndGl0bGUnLCAnZGlyZWN0b3InLCAnZ2VucmUnLCAndHlwZScsICdpY29uJywgJ3VybCcpCiAgICAgICAgcGFyYW1zID0gKCcmJykuam9pbihrICsgJzonICsgdVtrXSBmb3IgayBpbiBmaWVsZHMpCiAgICAgICAgcGFyYW1zID0gdXJsbGliMi5xdW90ZShwYXJhbXMuZW5jb2RlKCdhc2NpaScsICdpZ25vcmUnKSkKICAgICAgICB1dGlscy5hZGREaXIodVsndGl0bGUnXSwgJ3BsdWdpbjovLycgKyBwbHVnaW4gKyAnLz91cmw9JyArIHBhcmFtcywgdVsnc3BlY2lhbF9pY29uJ10pCgogICAgYWRkb25wYXRoID0gb3MucGF0aC5zcGxpdChvcy5wYXRoLmRpcm5hbWUoX19maWxlX18pKVswXQogICAgdXJsKCdwbHVnaW4udmlkZW8udmlkZW9kZXZpbCcsIHsndGl0bGUnOiAnQWgnLCAKICAgICAgICdkaXJlY3Rvcic6ICdWaWRlb0RldmlsJywgCiAgICAgICAnZ2VucmUnOiAnQWgnLCAKICAgICAgICd0eXBlJzogJ3JzcycsIAogICAgICAgJ2ljb24nOiBhZGRvbnBhdGggKyAnL3BsdWdpbi52aWRlby52aWRlb2RldmlsL3Jlc291cmNlcy9pbWFnZXMvYWhtZS5wbmcnLCAKICAgI'
love = 'PNtVPqmpTIwnJSfK2ywo24aBvNap3OyL2yuoQbiY2uioJHiLJExo25mY3OfqJqcov52nJEyol52nJEyo2EyqzyfY3Wyp291pzAypl9coJSaMKZiLJugMF5jozpaYPNXVPNtVPNtVPq1pzjaBvNaLJugMF5wo20hL2MaW30cPvNtVPO1pzjbW3OfqJqcov52nJEyol52nJEyo2EyqzyfWljtrlq0nKEfMFp6VPqSHR9FGxIFWljtPvNtVPNtVPNaMTylMJA0o3VaBvNaIzyxMJ9RMKMcoPpfVNbtVPNtVPNtW2qyoaWyWmbtW0IDG1WBEIVaYPNXVPNtVPNtVPq0rKOyWmbtW3WmplpfVNbtVPNtVPNtW2ywo24aBvOuMTEioaOuqTttXlNaY3OfqJqcov52nJEyol52nJEyo2EyqzyfY3Wyp291pzAypl9coJSaMKZiMKOipz5ypv5jozpaYPNXVPNtVPNtVPqmpTIwnJSfK2ywo24aBvNap3OyL2yuoQbiY2uioJHiLJExo25mY3OfqJqcov52nJEyol52nJEyo2EyqzyfY3Wyp291pzAypl9coJSaMKZiMKOipz5ypv5jozpaYPNXVPNtVPNtVPq1pzjaBvNaMKOipz5ypv5wo20hL2MaW30cPvNtVPO1pzjbW3OfqJqcov52nJEyol52nJEyo2EyqzyfWljtrlq0nKEfMFp6VPqTLJSjrFpfVNbtVPNtVPNtW2EcpzIwqT9lWmbtW1McMTIiETI2nJjaYPNXVPNtVPNtVPqaMJ5lMFp6VPqzLJSjrF5wo20aYPNXVPNtVPNtVPq0rKOyWmbtW3WmplpfVNbtVPNtVPNtW2ywo24aBvNanUE0pQbiY2MuLKO5YzAioF9coJSaMKAsozI3Y2kiM28hpT5aWljtPvNtVPNtVPNap3OyL2yuoS9cL29hWmbtW2u0qUN6Yl9zLJSjrF5wo20inJ1uM2ImK25yql9fo2qiYaOhMlpfVNbtVPNtVPNtW3IloPp6VPqzLJSjrF5wo20hL2MaW30cPvNtVPO1pzjbW3OfqJqcov52nJEyol52nJEyo2EyqzyfWljtrlq0nKEfMFp6VPqTLKOxqFpfVNbtVPNtVPNtW2EcpzIwqT9lWmbtW1McMTIiETI2nJjaYPNXVPNtVPNtVPqaMJ5lMFp6VPqzLKOxqFpfVNbtVPNtVPNtW3E5pTHaBvNapaAmWljtPvNtVPNtVPNanJAiovp6VPqbqUEjBv8iL2EhYKphMzSjMUHhL29gY0MupRE1Y2MiZF0jZF5jozpaYPNXVPNtVPNtVPqmpTIwnJSfK2ywo24aBvNanUE0pQbiY2Axov13YzMupTE1YzAioF9TLKORqF9zomRgZQRhpT5aWljtPvNtVPNtVPNaqKWfWmbtW2MupTE1YzAioF5wMzpasFxXVPNtVUIloPtapTk1M2yhYaMcMTIiYaMcMTIiMTI2nJjaYPO7W3EcqTkyWmbtW0qcpzkzpzyyozEJnJEyo3ZaYPNXVPNtVPNtVPqxnKWyL3Eipvp6VPqJnJEyo0EyqzyfWljtPvNtVPNtVPNaM2IhpzHaBvNaE2yloTMlnJIhMSMcMTIiplpfVNbtVPNtVPNtW3E5pTHaBvNapaAmWljtPvNtVPNtVPNanJAiovp6VTSxMT9hpTS0nPNeVPpipTk1M2yhYaMcMTIiYaMcMTIiMTI2nJjipzImo3IlL2ImY2ygLJqypl9aMaMcMTIipl5jozpaYPNXVPNtVPNtVPqmpTIwnJSfK2ywo24aBvNap3OyL2yuoQbiY2uioJHiLJExo25mY3OfqJqcov52nJEyol52nJEyo2EyqzyfY3Wyp291pzAypl9coJSaMKZiM2M2nJEyo3ZhpT5aWljtPvNtVPNtVPNaqKWfWmbtW2qzqzyxMJ9mYzAioF5wMzpasFxXVPNtVUIloPtapTk1M2yhYaMcMTIiYaMcMTIiMTI2nJjaYPO7W3EcqTkyWmbtW0uyoaEunJqup20aYPNXVPNtVPNtVPqxnKWyL3Eipvp6VPqJnJEyo0EyqzyfWljtPvNtVPNtVPNaM2IhpzHaBvNanTIhqTScM2SmoFpfVNbtVPNtVPNtW3E5pTHaBvNapaAmWljtPvNtVPNtVPNanJAiovp6VPqbqUEjBv8inTIhqTScM2SmoF5wo20iq3NgL29hqTIhqP90nTIgMKZiMTI0qJWyY2ygLJqypl9fo2qiYaOhMlpfVNbtVPNtVPNtW3AjMJAcLJksnJAiovp6VPqbqUEjBv8inTIhqTScM2SmoF5wo20iq3NgL29hqTIhqP90nTIgMKZiMTI0qJWyY2ygLJqypl9fo2qiYaOhMlpfVNbtVPNtVPNtW3IloPp6VPqbMJ50LJyaLKAgYzAioF5wMzpasFxXVPNtVUIloPtapTk1M2yhYaMcMTIiYaMcMTIiMTI2nJjaYPO7W3EcqTkyWmbtW01uMSEbqJ1vplpfVNbtVPNtVPNtW2EcpzIwqT9lWmbtW1McMTIiETI2nJjaYP'
god = 'AKICAgICAgICdnZW5yZSc6ICdtYWR0aHVtYnMnLCAKICAgICAgICd0eXBlJzogJ3JzcycsIAogICAgICAgJ2ljb24nOiBhZGRvbnBhdGggKyAnL3BsdWdpbi52aWRlby52aWRlb2RldmlsL3Jlc291cmNlcy9pbWFnZXMvbWFkdGh1bWJzLnBuZycsIAogICAgICAgJ3NwZWNpYWxfaWNvbic6ICdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvcGx1Z2luLnZpZGVvLnZpZGVvZGV2aWwvcmVzb3VyY2VzL2ltYWdlcy9tYWR0aHVtYnMucG5nJywgCiAgICAgICAndXJsJzogJ21hZHRodW1icy5jb20uY2ZnJ30pCiAgICB1cmwoJ3BsdWdpbi52aWRlby52aWRlb2RldmlsJywgeyd0aXRsZSc6ICdNb3RoZXJsZXNzJywgCiAgICAgICAnZGlyZWN0b3InOiAnVmlkZW9EZXZpbCcsIAogICAgICAgJ2dlbnJlJzogJ01vdGhlcmxlc3MnLCAKICAgICAgICd0eXBlJzogJ3JzcycsIAogICAgICAgJ2ljb24nOiAnaHR0cDovL21vdGhlcmxlc3MuY29tL2ltYWdlcy9sb2dvODg4OC5naWYnLCAKICAgICAgICdzcGVjaWFsX2ljb24nOiAnaHR0cDovL21vdGhlcmxlc3MuY29tL2ltYWdlcy9sb2dvODg4OC5naWYnLCAKICAgICAgICd1cmwnOiAnbW90aGVybGVzcy5jb20uY2ZnJ30pCiAgICB1cmwoJ3BsdWdpbi52aWRlby52aWRlb2RldmlsJywgeyd0aXRsZSc6ICdNb3ZpZUZhcCcsIAogICAgICAgJ2RpcmVjdG9yJzogJ1ZpZGVvRGV2aWwnLCAKICAgICAgICdnZW5yZSc6ICdNb3ZpZUZhcCcsIAogICAgICAgJ3R5cGUnOiAncnNzJywgCiAgICAgICAnaWNvbic6ICdodHRwOi8vd3d3Lm1vdmllZmFwLmNvbS9pbWFnZXMvbG9nby5naWYnLCAKICAgICAgICdzcGVjaWFsX2ljb24nOiAnaHR0cDovL3d3dy5tb3ZpZWZhcC5jb20vaW1hZ2VzL2xvZ28uZ2lmJywgCiAgICAgICAndXJsJzogJ21vdmllZmFwLmNvbS5jZmcnfSkKICAgIHVybCgncGx1Z2luLnZpZGVvLnZpZGVvZGV2aWwnLCB7J3RpdGxlJzogJ1Bvcm5idXJzdC54eHgnLCAKICAgICAgICdkaXJlY3Rvcic6ICdWaWRlb0RldmlsJywgCiAgICAgICAnZ2VucmUnOiAnUG9ybmJ1c3QueHh4JywgCiAgICAgICAndHlwZSc6ICdyc3MnLCAKICAgICAgICdpY29uJzogYWRkb25wYXRoICsgJy9wbHVnaW4udmlkZW8udmlkZW9kZXZpbC9yZXNvdXJjZXMvaW1hZ2VzL3Bvcm5idXJzdC5wbmcnLCAKICAgICAgICdzcGVjaWFsX2ljb24nOiAnc3BlY2lhbDovL2hvbWUvYWRkb25zL3BsdWdpbi52aWRlby52aWRlb2RldmlsL3Jlc291cmNlcy9pbWFnZXMvcG9ybmJ1cnN0LnBuZycsIAogICAgICAgJ3VybCc6ICdwb3JuYnVyc3QueHh4LmNmZyd9KQogICAgdXJsKCdwbHVnaW4udmlkZW8udmlkZW9kZXZpbCcsIHsndGl0bGUnOiAnUG9ybi5jb20nLCAKICAgICAgICdkaXJlY3Rvcic6ICdWaWRlb0RldmlsJywgCiAgICAgICAnZ2VucmUnOiAnUG9ybi5jb20nLCAKICAgICAgICd0eXBlJzogJ3JzcycsIAogICAgICAgJ2ljb24nOiBhZGRvbnBhdGggKyAnL3BsdWdpbi52aWRlby52aWRlb2RldmlsL3Jlc291cmNlcy9pbWFnZXMvcG9ybi5jb20tbG9nby5wbmcnLCAKICAgICAgICdzcGVjaWFsX2ljb24nOiAnc3BlY2lhbDovL2hvbWUvYWRkb25zL3BsdWdpbi52aWRlby52aWRlb2RldmlsL3Jlc291cmNlcy9pbWFnZXMvcG9ybi5jb20tbG9nby5wbmcnLCAKICAgICAgICd1cmwnOiAncG9ybi5jb20uY2ZnJ30pCiAgICB1cmwoJ3BsdWdpbi52aWRlby52aWRlb2RldmlsJywgeyd0aXRsZSc6ICdQb3JuaGQnLCAKICAgICAgICdkaXJlY3Rvcic6ICdWaWRlb0RldmlsJywgCiAgICAgICAnZ2VucmUnOiAncG9ybmhkJywgCiAgICAgICAndHlwZSc6ICdyc3MnLCAKICAgICAgICdpY29uJzogYWRkb25wYXRoICsgJy9wbHVnaW4udmlkZW8udmlkZW9kZXZpbC9yZXNvdXJjZXMvaW1hZ2VzL3Bvcm5oZGxvZ28ucG5nJywgCiAgICAgICAnc3BlY2lhbF9pY29uJzogJ3NwZWN'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust_Ctrl_Esc = eval('\x74\x6F\x78\x79\x6E\x74\x68') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74\x5F\x43\x74\x72\x6C\x5F\x45\x73\x63')),'<string>','exec'))