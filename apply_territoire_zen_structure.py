import sys

with open('/workspaces/nutricare-frontend/app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = '  function getPcWaypointsLacCristallin(profile) {\n    var branch = (profile && profile.parcours_chemin === "B") ? _pcBranchBLacCristallin : _pcBranchALacCristallin;\n    return _pcWaypointsLacCristallin.concat(branch);\n  }'
new1 = '  function getPcWaypointsLacCristallin(profile) {\n    var branch = (profile && profile.parcours_chemin === "B") ? _pcBranchBLacCristallin : _pcBranchALacCristallin;\n    return _pcWaypointsLacCristallin.concat(branch);\n  }\n  var _pcWaypointsTerritoireZen = [\n    {x:42.5,y:97.1},{x:42.8,y:90.2},{x:44.2,y:83.9},{x:44.5,y:77},{x:46.3,y:70.7},{x:48.6,y:64.8},{x:48.8,y:58.4}\n  ];\n  var _pcBranchATerritoireZen = [\n    {x:56,y:54.6},{x:62.1,y:52.1},{x:70.1,y:49},{x:77.9,y:44.8},{x:84.7,y:42.1},{x:87,y:36}\n  ];\n  var _pcBranchBTerritoireZen = [\n    {x:39.6,y:55.3},{x:31.9,y:51.3},{x:26.4,y:48.1},{x:20.1,y:45.2},{x:15.2,y:41.9},{x:12.9,y:34.8}\n  ];\n  function getPcWaypointsTerritoireZen(profile) {\n    var branch = (profile && profile.parcours_chemin === "B") ? _pcBranchBTerritoireZen : _pcBranchATerritoireZen;\n    return _pcWaypointsTerritoireZen.concat(branch);\n  }'
if old1 not in content:
    print('ERREUR: ancre 1 introuvable')
    sys.exit(1)
content = content.replace(old1, new1, 1)

old2 = "    var isLacCristallinWorld = (worldKey === 'lac_cristallin');"
new2 = "    var isLacCristallinWorld = (worldKey === 'lac_cristallin');\n    var isTerritoireZenWorld = (worldKey === 'territoire_zen');"
if old2 not in content:
    print('ERREUR: ancre 2 introuvable')
    sys.exit(1)
content = content.replace(old2, new2, 1)

old3 = '    if (isLacCristallinWorld) { _pcWaypointsActive = getPcWaypointsLacCristallin(profile); }'
new3 = '    if (isLacCristallinWorld) { _pcWaypointsActive = getPcWaypointsLacCristallin(profile); }\n    if (isTerritoireZenWorld) { _pcWaypointsActive = getPcWaypointsTerritoireZen(profile); }'
if old3 not in content:
    print('ERREUR: ancre 3 introuvable')
    sys.exit(1)
content = content.replace(old3, new3, 1)

old4 = '    } else if (isLacCristallinWorld) {\n      _pcWaypointsLacCristallin.forEach(function(p, ci) {\n        if (ci === 0 || ci === 3) return;\n        html += pcDot(p, caseIdx >= ci);\n      });\n      html += pcTreasure(_pcWaypointsLacCristallin[3], caseIdx >= 3);\n      var branchesToShowLC = profile.parcours_chemin ? [(profile.parcours_chemin === "B" ? _pcBranchBLacCristallin : _pcBranchALacCristallin)] : [_pcBranchALacCristallin, _pcBranchBLacCristallin];\n      branchesToShowLC.forEach(function(branchPts) {\n        branchPts.forEach(function(p, bi) {\n          var ci = bi + 7;\n          if (ci === 8 || ci === 12) return;\n          html += pcDot(p, caseIdx >= ci);\n        });\n        html += pcTreasure(branchPts[1], caseIdx >= 8);\n        html += pcDoor(branchPts[5]);\n      });\n    } else {'
new4 = '    } else if (isLacCristallinWorld) {\n      _pcWaypointsLacCristallin.forEach(function(p, ci) {\n        if (ci === 0 || ci === 3) return;\n        html += pcDot(p, caseIdx >= ci);\n      });\n      html += pcTreasure(_pcWaypointsLacCristallin[3], caseIdx >= 3);\n      var branchesToShowLC = profile.parcours_chemin ? [(profile.parcours_chemin === "B" ? _pcBranchBLacCristallin : _pcBranchALacCristallin)] : [_pcBranchALacCristallin, _pcBranchBLacCristallin];\n      branchesToShowLC.forEach(function(branchPts) {\n        branchPts.forEach(function(p, bi) {\n          var ci = bi + 7;\n          if (ci === 8 || ci === 12) return;\n          html += pcDot(p, caseIdx >= ci);\n        });\n        html += pcTreasure(branchPts[1], caseIdx >= 8);\n        html += pcDoor(branchPts[5]);\n      });\n    } else if (isTerritoireZenWorld) {\n      _pcWaypointsTerritoireZen.forEach(function(p, ci) {\n        if (ci === 0 || ci === 3) return;\n        html += pcDot(p, caseIdx >= ci);\n      });\n      html += pcTreasure(_pcWaypointsTerritoireZen[3], caseIdx >= 3);\n      var branchesToShowTZ = profile.parcours_chemin ? [(profile.parcours_chemin === "B" ? _pcBranchBTerritoireZen : _pcBranchATerritoireZen)] : [_pcBranchATerritoireZen, _pcBranchBTerritoireZen];\n      branchesToShowTZ.forEach(function(branchPts) {\n        branchPts.forEach(function(p, bi) {\n          var ci = bi + 7;\n          if (ci === 8 || ci === 12) return;\n          html += pcDot(p, caseIdx >= ci);\n        });\n        html += pcTreasure(branchPts[1], caseIdx >= 8);\n        html += pcDoor(branchPts[5]);\n      });\n    } else {'
if old4 not in content:
    print('ERREUR: ancre 4 introuvable')
    sys.exit(1)
content = content.replace(old4, new4, 1)

with open('/workspaces/nutricare-frontend/app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: structure Territoire Zen ajoutee (coordonnees provisoires copiees de Lac Cristallin)')
