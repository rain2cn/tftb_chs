local set = {}
set.name = "Borderlands101"
set.setName = "Borderlands101"
set.descriptionFilenameOverride = ""
set.logicalName = "<Borderlands101>"
set.logicalDestination = "<>"
set.priority = 41
set.localDir = _currentDirectory
set.enableMode = "bootable"
set.version = "trunk"
set.descriptionPriority = 0
set.gameDataName = "Borderlands101 Game Data"
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
    _currentDirectory .. "Borderlands_pc_chs_full_Borderlands101.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands101_anichore.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands101_data.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands101_ms.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands101_txmesh.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands101_voice.ttarch2"
}
RegisterSetDescription(set)
