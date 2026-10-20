local set = {}
set.name = "Borderlands103"
set.setName = "Borderlands103"
set.descriptionFilenameOverride = ""
set.logicalName = "<Borderlands103>"
set.logicalDestination = "<>"
set.priority = 43
set.localDir = _currentDirectory
set.enableMode = "bootable"
set.version = "trunk"
set.descriptionPriority = 0
set.gameDataName = "Borderlands103 Game Data"
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
    _currentDirectory .. "Borderlands_pc_chs_full_Borderlands103.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands103_anichore.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands103_data.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands103_ms.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands103_txmesh.ttarch2",
    _currentDirectory .. "Borderlands_pc_Borderlands103_voice.ttarch2"
}
RegisterSetDescription(set)
