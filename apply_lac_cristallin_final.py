import sys

with open('/workspaces/nutricare-frontend/app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = '  var _pcWaypointsLacCristallin = [\n    {x:41,y:97},{x:44,y:91},{x:48,y:84},{x:50,y:76},{x:52,y:68},{x:49,y:60},{x:47,y:52},{x:57,y:48},{x:43,y:45},{x:66,y:44},{x:32,y:41},{x:78,y:37},{x:87,y:33}\n  ];\n  function getPcWaypointsLacCristallin(profile) {\n    return _pcWaypointsLacCristallin;\n  }'
new1 = '  var _pcWaypointsLacCristallin = [\n    {x:39.1,y:96.3},{x:41.7,y:89.5},{x:43.3,y:83.4},{x:44.5,y:76.8},{x:45.9,y:71},{x:47.5,y:64.7},{x:48.3,y:58.6}\n  ];\n  var _pcBranchALacCristallin = [\n    {x:56.1,y:54.7},{x:63.3,y:51.5},{x:71.9,y:48.2},{x:79.3,y:44.6},{x:86.1,y:40.9},{x:87.1,y:35.3}\n  ];\n  var _pcBranchBLacCristallin = [\n    {x:41.9,y:55.3},{x:35.5,y:52.1},{x:29.9,y:48.6},{x:23.5,y:45.7},{x:17.7,y:42.5},{x:12.7,y:38.6}\n  ];\n  function getPcWaypointsLacCristallin(profile) {\n    var branch = (profile && profile.parcours_chemin === "B") ? _pcBranchBLacCristallin : _pcBranchALacCristallin;\n    return _pcWaypointsLacCristallin.concat(branch);\n  }'

if old1 not in content:
    print('ERREUR: ancre 1 introuvable')
    sys.exit(1)
content = content.replace(old1, new1, 1)

old2 = '    } else if (isLacCristallinWorld) {\n      _pcWaypointsLacCristallin.forEach(function(p, ci) {\n        if (ci === 0 || ci === 4 || ci === 8 || ci === 12) return;\n        html += pcDot(p, caseIdx >= ci);\n      });\n      html += pcTreasure(_pcWaypointsLacCristallin[4], caseIdx >= 4);\n      html += pcTreasure(_pcWaypointsLacCristallin[8], caseIdx >= 8);\n      html += pcDoor(_pcWaypointsLacCristallin[12]);\n    } else {'
new2 = '    } else if (isLacCristallinWorld) {\n      _pcWaypointsLacCristallin.forEach(function(p, ci) {\n        if (ci === 0 || ci === 4) return;\n        html += pcDot(p, caseIdx >= ci);\n      });\n      html += pcTreasure(_pcWaypointsLacCristallin[4], caseIdx >= 4);\n      var branchesToShowLC = profile.parcours_chemin ? [(profile.parcours_chemin === "B" ? _pcBranchBLacCristallin : _pcBranchALacCristallin)] : [_pcBranchALacCristallin, _pcBranchBLacCristallin];\n      branchesToShowLC.forEach(function(branchPts) {\n        branchPts.forEach(function(p, bi) {\n          var ci = bi + 7;\n          if (ci === 8 || ci === 12) return;\n          html += pcDot(p, caseIdx >= ci);\n        });\n        html += pcTreasure(branchPts[1], caseIdx >= 8);\n        html += pcDoor(branchPts[5]);\n      });\n    } else {'

if old2 not in content:
    print('ERREUR: ancre 2 introuvable')
    sys.exit(1)
content = content.replace(old2, new2, 1)

with open('/workspaces/nutricare-frontend/app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: Lac Cristallin reconstruit avec tronc commun + 2 branches, coordonnees exactes')
