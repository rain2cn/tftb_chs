local set = {}
set.name = "Borderlands102"
set.setName = "Borderlands102"
set.descriptionFilenameOverride = ""
set.logicalName = "<Borderlands102>"
set.logicalDestination = "<>"
set.priority = 42
set.localDir = _currentDirectory
set.enableMode = "bootable"
set.version = "trunk"
set.descriptionPriority = 0
set.gameDataName = "Borderlands102 Game Data"
set.gameDataPriority = 0
set.gameDataEnableMode = "constant"
set.localDirIncludeBase = true
set.localDirRecurse = false
set.localDirIncludeOnly = nil
set.localDirExclude = 
{
    "_dev/"
}
set.gameDataArchives = 
{
    _currentDirectory .. "Borderlands_pc_chs_full_Borderlands102.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands102_anichore.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands102_data.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands102_ms.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands102_txmesh.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands102_voice.ttarch2"
}
RegisterSetDescription(set)
