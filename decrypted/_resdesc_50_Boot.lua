local set = {}
set.name = "Boot"
set.setName = "Boot"
set.descriptionFilenameOverride = ""
set.logicalName = "<Boot>"
set.logicalDestination = "<>"
set.priority = 10
set.localDir = _currentDirectory
set.enableMode = "bootable"
set.version = "trunk"
set.descriptionPriority = 0
set.gameDataName = "Boot Game Data"
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
    _currentDirectory .. "Borderlands_pc_chs_full_Boot.ttarch2",
    _currentDirectory .. "Borderlands_pc_Boot_anichore.ttarch2",
    _currentDirectory .. "Borderlands_pc_Boot_data.ttarch2",
    _currentDirectory .. "Borderlands_pc_Boot_ms.ttarch2",
    _currentDirectory .. "Borderlands_pc_Boot_txmesh.ttarch2"
}
RegisterSetDescription(set)
