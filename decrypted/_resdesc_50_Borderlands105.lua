local set = {}
set.name = "Borderlands105"
set.setName = "Borderlands105"
set.descriptionFilenameOverride = ""
set.logicalName = "<Borderlands105>"
set.logicalDestination = "<>"
set.priority = 45
set.localDir = _currentDirectory
set.enableMode = "bootable"
set.version = "trunk"
set.descriptionPriority = 0
set.gameDataName = "Borderlands105 Game Data"
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
    _currentDirectory .. "Borderlands_pc_chs_full_Borderlands105.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands105_anichore.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands105_data.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands105_ms.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands105_txmesh.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands105_voice.ttarch2"
}
RegisterSetDescription(set)
